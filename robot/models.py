# coding: utf-8
from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    likes = models.TextField(help_text="喜欢吃的菜关键字，使用'|'分割，eg.宫保鸡丁|孜然肥牛")
    dislikes = models.TextField(help_text="不喜欢吃的菜关键字，使用'|'分割，eg.宫保鸡丁|孜然肥牛")
    online = models.BooleanField(default=True)

