#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import time
import uuid
import hashlib

from datetime import datetime


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


class Pagination(object):
    def __init__(self, page, page_size):
        self._page = page
        self._page_size = page_size

    @property
    def page_size(self):
        return self._page_size

    @property
    def start(self):
        return self._page_size * (self._page - 1)


class FileNameGenerator(object):
    """文件名称生成器"""

    @staticmethod
    def generate():
        datetime_template = "{year}/{month}/{day}/"
        today = datetime.today()
        datetime_template = datetime_template.format(
            year=today.year,
            month=today.month,
            day=today.day
        )

        return datetime_template + str(int(time.time()))


class PasswordGenerator(object):
    """密码生成器"""

    def __init__(self, password, salt=None):
        self._password = password
        if not salt:
            self._salt = str(uuid.uuid4())
        else:
            self._salt = salt

    def generate(self):
        m = hashlib.sha256()
        m.update(self._password.encode("utf-8"))
        m.update(self._salt.encode("utf-8"))
        return m.hexdigest()

    def get_salt(self):
        return self._salt
