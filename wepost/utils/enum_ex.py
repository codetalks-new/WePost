# coding=utf-8
from enum import Enum


class ChoiceEnum(Enum):
    @property
    def label(self):
        return self.name

    @classmethod
    def choices(cls):
        return [(it.value, it.label) for it in list(cls)]


class StrEnum(str, ChoiceEnum):
    """is a str and a enum"""

    def __str__(self):
        return self.value


class IntEnum(int, ChoiceEnum):
    """is a int and a enum"""

    def __str__(self):
        return self.value
