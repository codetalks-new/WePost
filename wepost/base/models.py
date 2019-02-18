# coding: utf-8
from django.db import models
from django.urls import reverse

__author__ = 'banxi'


class CreatedUpdatedMixin(models.Model):
  updated = models.DateTimeField(auto_now=True, verbose_name='最后更新')
  created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
  class Meta:
    abstract = True


class BaseReactStatMixin(models.Model):
  # 基本反馈统计相关数据
  like_count = models.PositiveIntegerField("喜欢数", default=0)
  dislike_count = models.PositiveIntegerField("不喜欢数", default=0)
  fav_count = models.PositiveIntegerField("收藏数", default=0)
  share_count = models.PositiveIntegerField("分享数", default=0)

  class Meta:
    abstract = True

class BaseModel(CreatedUpdatedMixin):
  class Meta:
    abstract = True

  @classmethod
  def get_admin_changelist_url(cls):
    app_label = cls._meta.app_label
    model_name = cls._meta.model_name
    info = (app_label, model_name)
    return reverse('admin:%s_%s_changelist' % info, current_app=None)
