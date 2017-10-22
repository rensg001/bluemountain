#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

class User(object):
    def __init__(self,
                 user_id,
                 username,
                 password,
                 salt,
                 retry,
                 is_valid):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.salt = salt
        self.retry = retry
        self.is_valid = is_valid