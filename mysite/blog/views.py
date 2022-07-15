from django.shortcuts import render_to_response,get_object_or_404,get_list_or_404

from blog.models import Blog,BlogType

from django.core.paginator import Paginator

from django.db.models import Sum,Count,Min,Max,Avg

from read_count.views import toBe_or_NotToBe

# 导入settings.py
from django.conf import settings


def get_blog_list_common(request, blogs):
    paginator = Paginator(blogs, settings.BLOGS_NUMBER_OF_EACH_PAGE)  # 基于5篇一页，进行划分于分页器
    page_num = request.GET.get("page", 1)  # 获取用户请求的page号
    page_of_blogs = paginator.get_page(page_num)  # 获取对应号于分页器上的内容（乱输入则为1）
    current_page_num = page_of_blogs.number  # 当前页码数

    # 进行分页下标的生成
    page_range = [num for num in range(current_page_num - 2, current_page_num + 3) if 0 < num <= paginator.num_pages]

    # 获取日期分类对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')  # ‘month’会返回年和月的日期
    blog_dates_dict = {}

    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month
                                         ).count()
        blog_dates_dict[blog_date] = blog_count

    context = {
        'page_of_blogs': page_of_blogs,  # 分页器
        'page_range': page_range,  # 分页器范围
        'blog_types': BlogType.objects.annotate(blog_count = Count('blog')),    # 显示总的博客分类及各分类下的博客数量
        'blog_dates': blog_dates_dict,
    }
    return context

def blog_detail(request,blog_id):# 性能硬伤
    blog_current = get_object_or_404(Blog, id=blog_id)

    read_cookie = toBe_or_NotToBe(request, blog_current)

    context = {
        'blog' : blog_current,
        'blog_previous' : Blog.objects.filter(created_time__gt=blog_current.created_time).last(),
        'blog_next' : Blog.objects.filter(created_time__lt=blog_current.created_time).first(),
    }

    response = render_to_response('blog/blog_detail.html', context)
    if read_cookie !='':    # 已读情况下，不刷新cookie的生存时间
        response.set_cookie(key=read_cookie, value='True', max_age=300)

    return response

def blog_list(request):
    blogs = Blog.objects.all()        # 获取需要的博文们blogs
    context = get_blog_list_common(request,blogs)   # 对blogs进行分页处理留一些必要的参数

    return render_to_response('blog/blog_list.html', context)



def blog_with_type(request,blog_type_id):
    blog_type = get_object_or_404(BlogType, id=blog_type_id)
    blogs = Blog.objects.filter(blog_type=blog_type)            # 获取需要的博文们blogs
    context = get_blog_list_common(request,blogs)

    context['blogs_with_type'] = blog_type                            # 分类类型    传到模板后，主要用于标识一些内容

    return render_to_response('blog/blog_with_type.html', context)

def blog_with_date(request, year, month):
    blogs = get_list_or_404(Blog, created_time__year=year, created_time__month=month)
    context = get_blog_list_common(request,blogs)

    context['blogs_with_date'] = '%s年%s月'%(year, month)         # 时间类型    传到模板后，主要用于标识一些内容

    return render_to_response('blog/blog_with_date.html', context)