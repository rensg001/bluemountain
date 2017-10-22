#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, SMALLINT
from ..base import ModelBase

class UserModel(ModelBase):
    """上传的文件"""

    __tablename__ = "user"

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    retry = Column(SMALLINT, nullable=False)
    is_valid = Column(Boolean, nullable=False)