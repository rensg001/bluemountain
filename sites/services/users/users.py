#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from sites.db.users import users as usersdb
from sites.services.users.entity import User

from .exceptions import UserNotMatchError
from ..base import PasswordGenerator

def create(username, password):

    pg = PasswordGenerator(password)
    user_info = User(
        user_id=None,
        username=username,
        password=pg.generate(),
        salt=pg.get_salt(),
        retry=0,
        is_valid=True
    )
    return usersdb.create(user_info)

def increase_retry(user_id):
    user_info = usersdb.get_one(user_id)
    user_info.retry += 1
    usersdb.update(user_info)


def validate(username, password):
    user_info = usersdb.get_by_username(username)
    if not user_info:
        raise UserNotMatchError("user does not matched.", 400)

    pg = PasswordGenerator(password, user_info.salt)
    if pg.generate() != user_info.password:
        increase_retry(user_info.user_id)
        raise UserNotMatchError("user does not matched.", 400)

    return user_info

def get_one(user_id):
    return usersdb.get_one(user_id)