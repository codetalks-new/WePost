#!/usr/bin/env python
# coding: utf-8
import os
import sys
import pytest

__author__ = '代码会说话'


def main():
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wepost.conf.test')
  # 以运行 runtests.py 的模式运行而不是直接以 pytest --cov wepost 是因为直接运行 pytest 会提示找不到 wepost 模块
  # 而已运行 runtests.py 的形式的话，python 会自动把此文件当前所在目录添加进 PYTHONPATH 中
  # sys.path.append(os.path.abspath('.'))
  return pytest.main(args=['--cov', 'wepost'])


if __name__ == '__main__':
  sys.exit(main())
