#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import datetime
from .entity import Log
from .exceptions import LogError
from ..base import Pagination
from ...db.logs import logs


def create(content):
    """创建日志"""

    # 日志长度检查
    if len(content) > 5000:
        raise LogError("日志内容超长", 400)

    now = datetime.datetime.now()
    log = Log(None, content, now.today(), now, None, True)
    return logs.create(log)


def get_with_paging(page, page_size):
    paging = Pagination(page, page_size)
    logs_info = logs.get_with_paging(paging)
    logs_count = logs.count()
    return logs_info, logs_count
