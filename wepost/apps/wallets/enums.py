# coding: utf-8
from wepost.utils.enum_ex import IntEnum
from enum import unique

__author__ = '代码会说话'


class WalletState(IntEnum):
  NEW = 0
  ACTIVE = 1
  STOP = 4


_wallet_state_to_text = {
  WalletState.NEW: "新建",
  WalletState.ACTIVE: "已激活",
  WalletState.STOP: "已停用"
}


class BillDirection(IntEnum):
  REVENUE = 1
  PAYMENT = 2

  @property
  def label(self):
    return _bill_direction_to_text[self]


_bill_direction_to_text = {
  BillDirection.REVENUE: "收益",
  BillDirection.PAYMENT: "支出"

}


@unique
class BillCategory(IntEnum):
  # 收入类
  CHECK_IN = 101  # 每日登录签到随机送金币：+（1~50铜币）
  ACTIVE_IN = 102  # 每日活跃度送金币：+(1~50铜币)
  REPLY_IN = 110  # 创建的主题收到回复： +（5+ 铜币)
  LIKE_IN = 111  # 收到感谢：+10铜币

  CREATE_POST_COST = 201  # 创建主题： - (20 + 25 *字符数/1000 铜币)
  CREATE_REPLY_COST = 202  # 创建回复: -(5+25 * 字符/1000 铜币)
  LIKE_COST = 211  # 发送感谢: -10 铜币

  @property
  def label(self):
    return _bill_category_to_text[self]


_bill_category_to_text = {
  BillCategory.CHECK_IN: "每日登录奖励",
  BillCategory.ACTIVE_IN: "每日活跃度奖励",
  BillCategory.REPLY_IN: "主题回复收益",
  BillCategory.LIKE_IN: "收到谢意",
  BillCategory.CREATE_POST_COST: "创建主题",
  BillCategory.CREATE_REPLY_COST: "创建回复",
  BillCategory.LIKE_COST: "发送谢意",
}
