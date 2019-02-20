# coding: utf-8
from wepost.utils.enum_ex import IntEnum

__author__ = '代码会说话'


class RelationState(IntEnum):
  FOLLOWING = 1  # 关注
  BLOCKING = 4  # 屏蔽

  @property
  def label(self):
    return _relation_state_to_text[self]


_relation_state_to_text = {
  RelationState.FOLLOWING: "关注",
  RelationState.BLOCKING: "屏蔽"
}
