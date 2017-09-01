#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import collections

from tornado.web import RequestHandler

from sites.services.base import UserExceptionBase


class BaseHandler(RequestHandler):
    """handler"""

    def write_error(self, status_code, **kwargs):

        exc_value = kwargs["exc_info"][1]
        if "exc_info" in kwargs and isinstance(
                exc_value,
                UserExceptionBase,
        ):
            self.write(ResponseResult(data=exc_value, code=400))
            self.finish()
        else:
            super(BaseHandler, self).write_error(status_code, **kwargs)


class ResponseResult(dict):
    """A dictionary that applies an arbitrary key-altering
       function before accessing the keys"""

    def __init__(self, data=None, code=200, *args, **kwargs):
        self.store = dict()
        # use the free update to set keys
        self.update(dict(data=data, code=code, *args, **kwargs))
        super(ResponseResult, self).__init__(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[self.__keytransform__(key)]

    def __setitem__(self, key, value):
        self.store[self.__keytransform__(key)] = value

    def __delitem__(self, key):
        del self.store[self.__keytransform__(key)]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

    def __keytransform__(self, key):
        return key
