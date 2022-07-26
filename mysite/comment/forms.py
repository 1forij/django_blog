from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from comment.models import Comment

class CommentForm(forms.Form):
    contenttype = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(
                            label=False,
                            min_length=3,
                            widget=CKEditorWidget(config_name='comment_ckeditor'),
                            error_messages={'required': '评论内容不能为空'}
                        )
    reply_comment_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'reply_comment_id'}))

    def clean(self):
        # 评论对象的验证
        contenttype = self.cleaned_data["contenttype"]
        object_id = self.cleaned_data["object_id"]
        try:
            model_class = ContentType.objects.get(model=contenttype).model_class()
            model_obj = model_class.objects.get(id=object_id)
            self.cleaned_data["content_object"] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError("评论对象不存在")

        return self.cleaned_data

    def clean_reply_comment_id(self):
        reply_comment_id = self.cleaned_data["reply_comment_id"]
        if reply_comment_id < 0:
            raise forms.ValidationError("回复出错")
        elif reply_comment_id == 0:
            self.cleaned_data['parents'] = None
        elif Comment.objects.filter(id=reply_comment_id).exists():
            self.cleaned_data['parents'] = Comment.objects.get(id=reply_comment_id)
        else:
            raise forms.ValidationError("回复出错")
        return reply_comment_id


    # def clean_text(self):
    #     # 评论不能为空的验证
    #     print("空")
    #     text = self.cleaned_data["text"]
    #     if len(text) <3 :
    #         raise forms.ValidationError("评论不能为空")
    #     return text