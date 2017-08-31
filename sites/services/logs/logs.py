#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import datetime
from .entity import Log
from .exceptions import LogError
from ...db.logs import logs


def create(content):
    """创建日志"""

    # 日志长度检查
    if len(content) > 5000:
        raise LogError("日志内容超长", 400)

    now = datetime.datetime.now()
    log = Log(None, content, now.today(), now, None, True)
    return logs.create(log)
