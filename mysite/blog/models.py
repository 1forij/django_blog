from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from read_count.models import ReadNumExpand

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    # 在被引用时显示自身字段的名称
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpand):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType ,on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User ,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog:%s>"%self.title

    class Meta:
        ordering = ['-created_time']