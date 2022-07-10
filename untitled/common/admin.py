# Register your models here.

from django.contrib import admin

from common.models import Customer

# 将models内的Customer表注册到管理界面
admin.site.register(Customer)