from django.shortcuts import render,redirect,HttpResponse,Http404
from comment.models import Comment

from comment.forms import CommentForm

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse


@login_required(login_url='/user_auth/login')
def update_comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_obj = Comment.objects.create(
                user = request.user,
                text = comment_form.cleaned_data["text"],
                content_object = comment_form.cleaned_data["content_object"]
            )
            # 如果是回复则多做一些标记
            parents = comment_form.cleaned_data['parents']
            if not parents is None:
                comment_obj.root = parents.root if not parents.root is None else parents
                comment_obj.parents = parents
                comment_obj.reply_to = parents.user
            comment_obj.save()



            ajax_data = {
                'status': 'SUCCESS',
                'username': comment_obj.user.username,
                'comment_time': comment_obj.comment_time.strftime('%Y-%m-%d %H:%M'),
                'text': comment_obj.text
            }
            if not parents is None:
                ajax_data['reply_to'] = comment_obj.reply_to.username
            else:
                ajax_data['reply_to'] = ''
            ajax_data['id'] = comment_obj.id

            return JsonResponse(ajax_data)
        else:
            ajax_data = {
                'status': 'ERROR',
                'message': list(comment_form.errors.values())[0][0]
            }
            return JsonResponse(ajax_data)
    else:
        raise Http404('亲：没有找到你需要的内容！')


    # user = request.user
    # text = request.POST.get('text')
    # contenttype = request.POST.get('contenttype')
    # object_id = int(request.POST.get('object_id'))
    # # 获取contenttype的对应的类
    # model_class = ContentType.objects.get(model=contenttype).model_class()
    # model_obj = model_class.objects.get(id=object_id)
    #
    # Comment.objects.create(user=user, text=text, content_object=model_obj)
    #
    # referer = request.META.get('HTTP_REFERER','/')
    #
    # return redirect(referer)