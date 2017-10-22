#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""用户模块"""
from sites.services.users.exceptions import UserNotMatchError
from sites.www.handlers.handler import BaseHandler

from sites.services.users import users


class UsersHandler(BaseHandler):
    """用户"""

    def get(self):
        message = self.get_argument("message", default="")
        self.clear_cookie(name="blueus")
        return self.render("users/login.html", message=message)

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        try:
            user_info = users.validate(username, password)
        except UserNotMatchError:
            self.redirect("/users?message=用户名或密码错误")
            return

        self.set_secure_cookie(
            name="blueus",
            value=str(user_info.user_id),
            expires_days=None
        )
        self.redirect("/")
        return