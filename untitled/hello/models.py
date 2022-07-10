from django.db import models

# Create your models here.
class Student(models.Model):
    # 客户名称
    name = models.CharField(max_length=20)

    # 班级
    the_class = models.CharField(max_length=10)

    # 宿舍
    dormitory = models.CharField(max_length=18)