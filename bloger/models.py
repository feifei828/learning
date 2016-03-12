# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100) #博客题目
    category = models.CharField(max_length=50, blank=True) #博客标签
    date_time = models.DateTimeField(auto_now_add=True) #博客日期
    content = models.TextField(blank=True, null=True) #博客正文

    def __unicode__(self):
        return self.title

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    class Meta:
        ordering = ['-date_time']


