#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sites.services.file_upload.entity import File
from sites.services.base import Pagination

from .model import FilesModel
from ..base import Session


def create(file: File) -> int:
    """创建文件"""

    file = FilesModel(file_id=file.file_id,
                      name=file.name,
                      size=file.size,
                      type=file.type_,
                      path=file.path,
                      is_valid=file.is_valid,
                      create_time=file.create_time)
    with Session() as session:
        session.add(file)
        session.commit()
        file_id = file.file_id

    return file_id

def get_all():
    """获取所有文件"""

    file_list = []
    with Session() as session:
        files = session.query(FilesModel).filter(FilesModel.is_valid).all()

    for file in files:
        f = File(
            file_id=file.file_id,
            name=file.name,
            type_=file.type,
            size=file.size,
            path=file.path,
            is_valid=file.is_valid,
            create_time=file.create_time
        )
        file_list.append(f)
    return file_list


def get_one(file_id):
    with Session() as session:
        file = session.query(FilesModel).get(file_id)

    return File(
        file_id=file.file_id,
        name=file.name,
        type_=file.type,
        size=file.size,
        path=file.path,
        is_valid=file.is_valid,
        create_time=file.create_time
    )