from django.db import models

# Create your models here.
from wepost.apps.auth.models import WepostUser
from wepost.apps.wallets.enums import BillDirection, BillCategory, WalletState
from wepost.base.models import BaseModel
from wepost.vendors.django_archive_mixin.mixins import SoftDeleteMixin


class Wallet(BaseModel,SoftDeleteMixin):
  user = models.OneToOneField(WepostUser,on_delete=models.PROTECT)
  balance = models.DecimalField("余额",max_digits=17, decimal_places=2, default=0)
  freeze = models.DecimalField("冻结",max_digits=17, decimal_places=2, default=0)
  state = models.PositiveSmallIntegerField("状态", choices=WalletState.choices(),default=WalletState.ACTIVE)

  class Meta:
    verbose_name = "钱包"
    verbose_name_plural = verbose_name


class Bill(BaseModel,SoftDeleteMixin):
  user = models.ForeignKey(WepostUser, on_delete=models.PROTECT, verbose_name="所属用户")
  direction = models.PositiveSmallIntegerField("收支方向",choices=BillDirection.choices())
  # 对于收到谢意类型则记录对应发送用户
  from_user = models.ForeignKey(WepostUser, null=True, on_delete=models.PROTECT, verbose_name="来源用户", related_name="+")
  category = models.PositiveSmallIntegerField("收支类别",choices=BillCategory.choices())
  amount = models.DecimalField("数额", max_digits=17, decimal_places=2)
  current_balance = models.DecimalField("当前余额",max_digits=17, decimal_places=2, default=0)
  current_freeze = models.DecimalField("当前冻结",max_digits=17, decimal_places=2, default=0)

  class Meta:
    verbose_name = "收支明细"
    verbose_name_plural = verbose_name
