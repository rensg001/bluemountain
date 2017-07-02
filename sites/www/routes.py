#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.routing import URLSpec as url
from sites.www.handlers import main
from sites.www.handlers import web_logs

handlers = [
    url(r"/", main.IndexPageHandler),
    url(r"/web-logs", web_logs.WebLogsHandler),
    url(r"/web-log", web_logs.WebLogHandler)
]
