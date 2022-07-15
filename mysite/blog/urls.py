from django.urls import path,re_path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.blog_list,name = 'blog_list'),
    path('detail/<int:blog_id>',views.blog_detail,name = "blog_detail"),
    path('relevant/<int:blog_type_id>',views.blog_with_type,name = "blog_relevant"),
    path('date/<int:year>/<int:month>',views.blog_with_date,name = 'blog_date'),
]