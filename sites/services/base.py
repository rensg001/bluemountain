#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class UserExceptionBase(Exception):
    """用户自定义异常基类"""

    def __init__(self, msg, code):
        self._msg = msg
        self._code = code

    @property
    def msg(self):
        return self._msg

    @property
    def code(self):
        return self._code
