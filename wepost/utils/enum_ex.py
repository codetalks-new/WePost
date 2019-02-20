# coding=utf-8
from enum import Enum


class EnumChoiceMixin:
    @property
    def label(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(it.value, it.label) for it in list(cls)]


# 注意顺序 ：
# new enumerations should be created as `EnumName([mixin_type, ...] [data_type,] enum_type)`

class StrEnum(EnumChoiceMixin, str, Enum):
    """is a str and a enum"""

    def __str__(self):
        return self.value


class IntEnum(EnumChoiceMixin, int, Enum):
    """is a int and a enum"""

    def __str__(self):
        return self.value
