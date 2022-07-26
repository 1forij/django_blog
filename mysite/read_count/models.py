from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions

from django.utils import timezone

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)

    # 获取Contenttype中记录的其他表（比如，可以选blog表）
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    # 对应模型的主键值（比如，blog的id），数值类型
    object_id = models.PositiveIntegerField()
    # 把content_type和object_id两个字段合并成一个通用的外键，存入Contenttype表
    content_object = GenericForeignKey('content_type', 'object_id')

class ReadNumExpand():
    def get_read_num(self):
        try:
            # 通过Contenttype获取Blog对象，用作查询时的content_type以及通过blog对象.id得到计数值(Contenttype有全部对象信息)
            blog_obj = ContentType.objects.get_for_model(self)
            # 利用上面提供的参数，进行博客浏览量的查询  且存在该博文计数信息
            readNum_obj = ReadNum.objects.get(content_type=blog_obj,object_id=self.id)

        except exceptions.ObjectDoesNotExist:# 查询，结果不存在该博文计数信息,给该博文创建计数信息，默认值为0
            readNum_obj = ReadNum.objects.create(content_type=blog_obj,object_id=self.id)

        return readNum_obj.read_num

class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)

    read_num = models.IntegerField(default=0)

    # 获取Contenttype中记录的其他表（比如，可以选blog表）
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    # 对应模型的主键值（比如，blog的id），数值类型
    object_id = models.PositiveIntegerField()
    # 把content_type和object_id两个字段合并成一个通用的外键，存入Contenttype表
    content_object = GenericForeignKey('content_type', 'object_id')
