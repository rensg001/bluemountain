#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import datetime

from sites.www import settings
from sites.services.base import FileNameGenerator
from sites.services.file_upload.entity import File
from sites.db.file_upload import file_upload as file_uploaddb

def create(name, size, content_type, content):
    """创建文件

    保存文件到操作系统并保存相关信息到数据库
    """
    relative_path = FileNameGenerator.generate()
    file_path = os.path.join(settings.upload_path, relative_path)

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    with open(file_path, mode="wb") as f:
        f.write(content)

    file = File(
        None,
        name=name,
        size=size,
        type_="OTHER",
        path=relative_path,
        is_valid=True,
        create_time=datetime.datetime.now()
    )
    return file_uploaddb.create(file)


def get_all():
    """获取所有文件"""

    file_list = file_uploaddb.get_all()
    file_list = [
        {
            "file_id": item.file_id,
            "name": item.name,
            "size": item.size,
            "create_time": item.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        for item in file_list
    ]
    data = {
        "total": len(file_list),
        "rows": file_list
    }
    return data

def get_one(file_id: int):
    file_info = file_uploaddb.get_one(file_id)
    real_path = os.path.join(settings.upload_path, file_info.path)
    setattr(file_info, "real_path", real_path)
    return file_info