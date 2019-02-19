# coding=utf-8
import json

from django import db
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile, FieldFile
from django.forms import model_to_dict
from django.http import JsonResponse

from .enum_ex import IntEnum, StrEnum


class MyJSONEncoder(DjangoJSONEncoder):

    def default(self, o):
        # TypeError: Object of type 'ImageFieldFile' is not JSON serializable
        if callable(getattr(o, "to_dict",None)):
            return o.to_dict()
        elif isinstance(o, FieldFile):
            if o:
                return o.url
            else:
                return None
        elif isinstance(o, (StrEnum, IntEnum)):
            return o.value
        elif isinstance(o, db.models.Model):
            return model_to_dict(o)
        return super().default(o)


def stringify(obj, indent: bool = False):
    return json.dumps(obj, ensure_ascii=False, indent=indent, cls=MyJSONEncoder)


def jsonify(*args, **kwargs):
    if args and kwargs:
        raise TypeError('jsonify() behavior undefined when passed both args and kwargs')
    elif len(args) == 1:  # single args are passed directly to dumps()
        data = args[0]
    else:
        data = args or kwargs
    return JsonResponse(data, encoder=MyJSONEncoder, json_dumps_params={'ensure_ascii': False})

def json_dumps_and_loads(obj):
    """用于测试"""
    json_str = stringify(obj)
    return json.loads(json_str)