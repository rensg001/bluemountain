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
        return self.render(
            "web-logs/web-logs.html",
            username="任山贵"
        )


class WebLogHandler(BaseHandler):
    """日志"""

    def get(self):
        return self.render("web-logs/web-log.html")

    def post(self):
        content = self.get_argument("content")
        logs.create(content)
        return ResponseResult()
