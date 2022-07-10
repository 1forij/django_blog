from django.db import models

# Create your models here.
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=20)

    # 联系电话
    phoneNumber = models.CharField(max_length=11)

    # 联系地址
    address = models.CharField(max_length=60)

    # Email
    email = models.EmailField(null=True)        # 可以为空值