#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""日志模块"""
from sites.www.handlers.handler import BaseHandler
from sites.www.handlers.handler import ResponseResult
from sites.services.logs import logs


class WebLogsHandler(BaseHandler):
    """日志列表"""

    def get(self):
        page = self.get_argument("page", _type=int, default=1)
        page_size = self.get_argument("page_size", _type=int, default=10)

        logs_info, logs_count = logs.get_with_paging(page, page_size)
        return self.render(
            "web-logs/web-logs.html",
            username="任山贵",
            logs_info=logs_info,
            logs_count=logs_count,
            page=page,
            page_size=page_size,
        )


class WebLogHandler(BaseHandler):
    """日志"""

    def get(self):

        return self.render("web-logs/web-log.html")

    def post(self):
        content = self.get_argument("content")
        logs.create(content)
        self.write(ResponseResult())
        self.finish()
        return
