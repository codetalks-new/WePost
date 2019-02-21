from django.db import models

# Create your models here.
from wepost.apps.auth.models import WepostUser
from wepost.apps.notifications.enums import NotificationCategory, NotificationLevel
from wepost.base.models import BaseModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Notification(BaseModel):
  """通知 模型设计参考自 django-notifications"""
  recipient = models.ForeignKey(WepostUser, on_delete=models.CASCADE, verbose_name="接收人")
  # django-notifications 中的 verb 一内容就体现在 category 中.
  category = models.BigIntegerField("类别", choices=NotificationCategory.choices())
  level = models.PositiveSmallIntegerField("级别", choices=NotificationLevel.choices(), default=NotificationLevel.INFO)
  unread = models.BooleanField("未读", db_index=True,default=True)
  # 配置泛型 actor 外键关联
  actor_content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name="notify_actor",
                                         on_delete=models.CASCADE)
  actor_object_id = models.CharField(max_length=255, blank=True, null=True)
  actor = GenericForeignKey('actor_content_type', 'actor_object_id')

  # 配置事件发生范围,如果是指发帖子的话，可以认为是关联到对应节点.
  target_content_type = models.ForeignKey(
    ContentType,
    related_name='notify_target',
    blank=True,
    null=True,
    on_delete=models.CASCADE
  )
  target_object_id = models.CharField(max_length=255, blank=True, null=True)
  target = GenericForeignKey('target_content_type', 'target_object_id')

  # 配置事件发生主体，以发贴来说，可以当作关联到具体的帖子
  action_object_content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                                 related_name='notify_action_object', on_delete=models.CASCADE)
  action_object_object_id = models.CharField(max_length=255, blank=True, null=True)
  action_object = GenericForeignKey('action_object_content_type', 'action_object_object_id')

  memo = models.TextField("备注", blank=True, null=True, help_text="可以用来保存简短的回复等内容")

  class Meta:
    verbose_name = "通知"
    verbose_name_plural = verbose_name