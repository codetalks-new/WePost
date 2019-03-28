#!/usr/bin/env python
# coding: utf-8
import os
import sys
import pytest

__author__ = '代码会说话'


def main():
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wepost.conf.test')
  return pytest.main(args=['--cov', 'wepost'])


if __name__ == '__main__':
  sys.exit(main())
