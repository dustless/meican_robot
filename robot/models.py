# coding: utf-8
from django.db import models

# Create your models here.


class Account(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    likes = models.TextField(blank=True, default="", help_text="喜欢吃的菜关键字，使用'|'分割，eg.宫保鸡丁|孜然肥牛")
    dislikes = models.TextField(blank=True, default="", help_text="不喜欢吃的菜关键字，使用'|'分割，eg.宫保鸡丁|孜然肥牛")
    online = models.BooleanField(default=True)

    def __unicode__(self):
        return self.username


class Config(models.Model):
    enable = models.BooleanField(default=True, help_text="是否允许自动点餐")

