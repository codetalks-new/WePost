from django.db import models

# Create your models here.
from wepost.apps.auth.models import WepostUser
from wepost.apps.sns.enums import UserRelationState
from wepost.base.models import BaseModel


class UserRelation(BaseModel):
  from_user = models.ForeignKey(WepostUser, on_delete=models.CASCADE, verbose_name="用户", related_name="fan")
  to_user = models.ForeignKey(WepostUser, on_delete=models.CASCADE, verbose_name="目标用户", related_name="idol")
  state = models.PositiveSmallIntegerField("状态", choices=UserRelationState.choices())

  class Meta:
    unique_together = ("from_user", "to_user")
    verbose_name = "关注与屏蔽"
    verbose_name_plural = verbose_name