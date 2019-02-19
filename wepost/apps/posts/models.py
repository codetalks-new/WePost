import uuid

from django.db import models
from mptt.models import MPTTModel,TreeForeignKey

from wepost.apps.auth.models import WepostUser
from wepost.apps.posts.enums import PostState
from wepost.base.models import BaseModel, BaseReactStatMixin
from wepost.vendors.django_archive_mixin.mixins import SoftDeleteMixin


class Node(MPTTModel,BaseModel):
  """节点"""
  parent = TreeForeignKey('self', null=True, blank=True, related_name="children", on_delete=models.CASCADE,
                          verbose_name="父节点")
  code = models.CharField("编码", max_length=32, unique=True)
  name = models.CharField("名称", max_length=32, unique=True)
  brief = models.CharField("简介", max_length=512, blank=True, null=True)
  order = models.IntegerField("排序值", default=0)
  # 统计相关数据
  star_count = models.PositiveIntegerField("收藏数",default=0)
  post_count = models.PositiveIntegerField("主题数",default=0)

  class Meta:
    verbose_name = "节点"
    verbose_name_plural = verbose_name


  def __init__(self,*args,**kwargs):
    super(Node, self).__init__(*args, **kwargs)
    if not self.name:
      self.name = self.code.capitalize()

  def __str__(self):
    return self.name


class Post(BaseModel, SoftDeleteMixin, BaseReactStatMixin):
  # 显示指定主键 设计成 uuid 是为了避免被直接遍历爬取
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  node = models.ForeignKey(Node, verbose_name="节点", on_delete=models.PROTECT)
  creator = models.ForeignKey(WepostUser, verbose_name="创建者", on_delete=models.PROTECT)
  title = models.CharField("标题", max_length=128)
  content = models.TextField("内容",max_length=40960)
  content_rendered = models.TextField("渲染内容",max_length=81920, default='')
  state = models.SmallIntegerField("状态", choices=PostState.choices(), default=PostState.DRAFT)
  # 运营相关
  order = models.IntegerField("排序",default=0)
  # 回复相关冗余
  last_reply_by = models.CharField("最后回复人",max_length=150, blank=True, default='')
  last_touched = models.DateTimeField(auto_now=True, verbose_name='最后活跃')
  reply_count = models.PositiveIntegerField("回复数", default=0)
  # 统计相关数据, 基本反应数据继承自 BaseReactStatMixin
  member_view_count = models.PositiveIntegerField("会员浏览数", default=0)
  other_view_count = models.PositiveIntegerField("网页浏览数", default=0)

  class Meta:
    verbose_name = "主题"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.title


class Reply(MPTTModel, BaseModel, SoftDeleteMixin, BaseReactStatMixin):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="主题")
  ref = TreeForeignKey('self', null=True, blank=True, related_name="replies", on_delete=models.SET_NULL,
                       verbose_name="引用")
  creator = models.ForeignKey(WepostUser, verbose_name="回复人", on_delete=models.PROTECT)
  content = models.TextField("内容", max_length=4096)
  content_rendered = models.TextField("渲染内容", max_length=8192, default='')
  #
  creator_name = models.CharField("回复人名", max_length=150)  # 冗余数据
  reply_from = models.CharField("回复人来源", max_length=64, help_text="用户来源地点等信息")
  reply_ip = models.GenericIPAddressField("回复IP")

  # 统计相关数据, 基本反应数据继承自 BaseReactStatMixin
  class Meta:
    verbose_name = "回复"
    verbose_name_plural = verbose_name
