# coding: utf-8
import mimetypes

__author__ = 'banxi'

_xlsx_minetypes = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","application/vnd.ms-excel"]

def is_excel(file_path:str) -> bool:
  minetype,_ = mimetypes.guess_type(file_path)
  return minetype in _xlsx_minetypes

