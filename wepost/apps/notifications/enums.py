# coding: utf-8
from wepost.utils.enum_ex import EnumChoiceMixin, IntEnum
from enum import IntFlag

__author__ = '代码会说话'


class NotificationCategory(EnumChoiceMixin, IntFlag):
  """通知类别"""
  RECEIVE_REPLY = 1 << 0  # 收到回复
  RECEIVE_MENTION = 1 << 1  # 收到 @
  RECEIVE_REPLY_LIKE = 1 << 2  # 收到回复感谢
  RECEIVE_POST_LIKE = 1 << 3  # 收到主题感谢
  RECEIVE_REPLY_FAV = 1 << 4  # 收到回复被收藏
  RECEIVE_POST_FAV = 1 << 5  # 收到主题被收藏
  FOLLOWED_USER_NEW_REPLY = 1 << 6  # 关注用户有了新回复
  FOLLOWED_USER_NEW_POST = 1 << 7  # 关注用户创建了新主题
  FOLLOWED_POST_NEW_REPLY = 1 << 8  # 关注的主题有了新回复
  FOLLOWED_NODE_NEW_POST = 1 << 9  # 关注的节点有了新主题

  @property
  def label(self):
    return _notification_category_to_text[self]


_notification_category_to_text = {
  NotificationCategory.RECEIVE_REPLY: "收到回复",
  NotificationCategory.RECEIVE_MENTION: "收到@",
  NotificationCategory.RECEIVE_REPLY_LIKE: "收到回复感谢",
  NotificationCategory.RECEIVE_POST_LIKE: "收到主题感谢",
  NotificationCategory.RECEIVE_REPLY_FAV: "收到回复收藏",
  NotificationCategory.RECEIVE_POST_FAV: "收到主题收藏",
  NotificationCategory.FOLLOWED_USER_NEW_REPLY: "关注用户有了新回复",
  NotificationCategory.FOLLOWED_USER_NEW_POST: "关注用户创建了新主题",
  NotificationCategory.FOLLOWED_POST_NEW_REPLY: "关注的主题有了新回复",
  NotificationCategory.FOLLOWED_NODE_NEW_POST: "关注的节点有了新主题",
}


class NotificationLevel(IntEnum):
  """通知级别"""
  INFO = 0
  SUCCESS = 1
  WARNING = 2
  ERROR = 3

  @property
  def label(self):
    return _notification_level_to_text[self]


_notification_level_to_text = {
  NotificationLevel.INFO: "消息",
  NotificationLevel.SUCCESS: "成功",
  NotificationLevel.WARNING: "警告",
  NotificationLevel.ERROR: "错误",
}
