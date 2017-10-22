#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean
from ..base import ModelBase

class FilesModel(ModelBase):
    """上传的文件"""

    __tablename__ = "files"

    file_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    path = Column(String, nullable=False)
    is_valid = Column(Boolean, nullable=False)
    create_time = Column(DateTime, nullable=False)