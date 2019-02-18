from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
from wepost.base.models import BaseModel

class Node(MPTTModel,BaseModel):
  """节点"""
  parent = TreeForeignKey('self', null=True, blank=True, related_name="children", on_delete=models.CASCADE,
                          verbose_name="父节点")
  code = models.CharField("编码", max_length=32, unique=True)
  name = models.CharField("名称", max_length=32, unique=True)
  order = models.IntegerField("排序值", default=0)
  star_count = models.PositiveIntegerField("收藏数",default=0)
  post_count = models.PositiveIntegerField("主题数",default=0)
  brief = models.CharField("简介", max_length=512, blank=True, null=True)

  class Meta:
    verbose_name = "节点"
    verbose_name_plural = verbose_name


  def __init__(self,*args,**kwargs):
    super(Node, self).__init__(*args, **kwargs)
    if not self.name:
      self.name = self.code.capitalize()

  def __str__(self):
    return self.name