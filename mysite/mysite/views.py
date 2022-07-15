from django.shortcuts import render_to_response

from django.contrib.contenttypes.models import ContentType
from blog.models import Blog

from django.utils import timezone
from read_count.views import readNum_recent_senven,hotest_blog


def index(request):
    today = timezone.now().date()
    contenttype = ContentType.objects.get_for_model(Blog)
    hot_blogs = {}

    hot_datas = hotest_blog(today, contenttype)
    for i in range(5):
        title = Blog.objects.get(id = hot_datas[i].get("object_id")).title
        hot_blogs [title] = hot_datas[i]

    dates, week_datas = readNum_recent_senven(today, contenttype)

    context = {
        'hot_blogs':hot_blogs,
        'week_datas':week_datas,
        'dates':dates,
    }

    return render_to_response('index.html',context)
