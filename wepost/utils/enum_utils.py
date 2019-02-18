# coding=utf-8
from enum import Enum


class StrEnum(str, Enum):
    """is a str and a enum"""

    def __str__(self):
        return self.value


class IntEnum(int, Enum):
    """is a int and a enum"""

    def __str__(self):
        return self.value
