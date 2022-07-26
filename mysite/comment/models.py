from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='comments')


    root = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name='root_comment')
    # 回复也是一种评论啊，只不过是评论   已有的评论
    # 所以，是回复Comment表，
    # 又可能，多条回复同一个评论，所以foreignkey
    parents = models.ForeignKey('self', null=True, on_delete=models.DO_NOTHING, related_name='parents_comment')
    reply_to = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING, related_name='replies')

    def __str__(self):
        return self.text