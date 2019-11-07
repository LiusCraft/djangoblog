# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 用户模型
# 采用的继承方式扩展用户信息
class User(AbstractUser):
    avatar = models.ImageField(upload_to='static/avatar/%Y/%m', default='static/avatar/default.png', max_length=200, verbose_name='头像')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username
    def __str__(self):
        return self.username

# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

# 分类
class Catagory(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='分类名称')
    isLink = models.BooleanField(default=False, verbose_name='显示在导航栏')
    index = models.IntegerField(default=999, verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    desc = models.CharField(max_length=255, verbose_name='文章描述')
    content = models.TextField('文章内容')
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class Link(models.Model):
    title = models.CharField(max_length=10, verbose_name='链接标题')
    href = models.CharField(max_length=255,verbose_name='链接地址')
    index = models.IntegerField(default=999, verbose_name='排序')

    class Meta:
        verbose_name = '链接'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title

class FrpsList(models.Model):
    token = models.CharField(max_length=30, verbose_name='线路密匙')
    name = models.CharField(max_length=30, verbose_name='线路名称')
    data = models.TextField(verbose_name='线路信息')
    message = models.CharField(max_length=255, verbose_name='线路公告')

    class Meta:
        verbose_name = 'Frp服务线路'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

