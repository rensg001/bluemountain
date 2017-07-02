#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""日志模块"""
from sites.www.handlers.handler import BaseHandler


class WebLogsHandler(BaseHandler):
    """日志列表"""

    def get(self):
        return self.render(
            "web-logs/web-logs.html",
            username="<script>alert('任山贵')</script>"
        )


class WebLogHandler(BaseHandler):
    """日志"""

    def get(self):
        return self.render("web-logs/web-log.html")
