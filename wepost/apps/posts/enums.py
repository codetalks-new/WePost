# coding: utf-8
from wepost.utils.enum_ex import IntEnum

__author__ = '代码会说话'


class PostState(IntEnum):
  # 基本状态
  DRAFT = 1
  PUBLISHED = 6

  @property
  def label(self):
    return _post_state_to_text[self]


_post_state_to_text = {
  PostState.DRAFT: "草稿",
  PostState.PUBLISHED: "已发布",
}
