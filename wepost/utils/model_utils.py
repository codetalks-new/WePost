# coding: utf-8
from django.db import models

__author__ = 'banxi'

def fields_to_names(*fields:models.Field):
    """提取对应字段参数列表返回字段名称元组，用于 Django Model Admin 中的字段配置"""
    names = []
    for field in fields:
        name = None
        try:
            name = field.field_name
        except AttributeError:
            try:
                name = field.field.name
            except AttributeError:
                pass
        if name:
            names.append(name)
    return tuple(names)
