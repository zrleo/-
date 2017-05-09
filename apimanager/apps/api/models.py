# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Api(models.Model):

    api_name = models.CharField(u'接口名称')
    request_url = models.CharField(u'请求地址', max_length=200)
    request_param = models.TextField(u'请求参数', default={})
    method = models.CharField(u'请求方法')
    response_data = models.CharField(u'返回结果', default={})
    create_time = models.DateTimeField(u'创建时间', auto_now=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
