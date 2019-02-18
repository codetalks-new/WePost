# coding: utf-8
from django.db import models
from django.urls import reverse

__author__ = 'banxi'


class BaseModel(models.Model):
  updated = models.DateTimeField(auto_now=True, verbose_name='最后更新')
  created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

  objects = models.Manager() # 默认查询器，再次添加，方便自动补全

  class Meta:
    abstract = True

  @classmethod
  def get_admin_changelist_url(cls):
    app_label = cls._meta.app_label
    model_name = cls._meta.model_name
    info = (app_label, model_name)
    return reverse('admin:%s_%s_changelist' % info, current_app=None)
