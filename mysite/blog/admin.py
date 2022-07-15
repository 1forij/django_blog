from django.contrib import admin

from blog.models import BlogType,Blog

# 用于展示类(表)的属性和方法
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_type','get_read_num','created_time','last_updated_time')

'''
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','blog')
'''