# coding: utf-8
from wepost.utils.enum_ex import IntEnum

__author__ = '代码会说话'


class UserRelationState(IntEnum):
  FOLLOWING = 1  # 关注
  BLOCKING = 4  # 屏蔽

  @property
  def label(self):
    return _user_relation_state_to_text[self]


_user_relation_state_to_text = {
  UserRelationState.FOLLOWING: "关注",
  UserRelationState.BLOCKING: "屏蔽"
}
