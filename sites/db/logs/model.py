#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from ..base import ModelBase


class LogsModel(ModelBase):
    """日志表"""
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)
    create_date = Column(Date, nullable=False)
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)
    is_valid = Column(Boolean, nullable=False)
