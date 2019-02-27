# coding: utf-8
from wepost.utils.enum_ex import StrEnum

__author__ = '代码会说话'


class SortDirection(StrEnum):
  """排序方式"""
  ASC = "asc"
  DESC = "desc"

  @property
  def label(self):
    return _sort_direction_to_text[self]


_sort_direction_to_text = {
  SortDirection.ASC: "升序",
  SortDirection.DESC: "降序"
}


class SortField:
  """排序元素"""

  def __init__(self, field: str, direction: SortDirection = SortDirection.ASC):
    self.field = field
    self.direction = direction

  @property
  def ordering(self):
    if self.direction == SortDirection.DESC:
      return "-" + self.field
    else:
      return self.field

  def __str__(self):
    return self.ordering

  def __repr__(self):
    return self.ordering
