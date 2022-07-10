# Register your models here.

from django.contrib import admin

from hello.models import Student

# 将hello/models内的Student表注册到管理界面
admin.site.register(Student)