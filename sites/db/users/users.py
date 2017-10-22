#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from sites.services.users.entity import User
from .model import UserModel
from ..base import Session


def create(user_info: User):
    with Session() as session:
        user = UserModel(
            user_id=user_info.user_id,
            username=user_info.username,
            password=user_info.password,
            salt=user_info.salt,
            retry=user_info.retry,
            is_valid=user_info.is_valid
        )
        session.add(user)
        session.commit()
        user_id = user.user_id
    return user_id


def get_by_username(username) -> User:
    with Session() as session:
        user = session.query(UserModel).filter(
            UserModel.username == username,
            UserModel.is_valid
        ).first()

        user_info = User(
            user_id=user.user_id,
            username=user.username,
            password=user.password,
            salt=user.salt,
            retry=user.retry,
            is_valid=user.is_valid
        )

    return user_info

def get_one(user_id):
    with Session() as session:
        user = session.query(UserModel).get(user_id)
        if not user:
            return None
        user_info = User(
            user_id=user.user_id,
            username=user.username,
            password=user.password,
            salt=user.salt,
            retry=user.retry,
            is_valid=user.is_valid
        )
    return user_info

def update(user_info: User):
    with Session() as session:
        user = session.query(UserModel).get(user_info.user_id)
        if user:
            user.username = user_info.username
            user.password = user_info.password
            user.retry = user_info.retry
            user.is_valid = user_info.is_valid
            user.salt = user_info.salt
        session.commit()