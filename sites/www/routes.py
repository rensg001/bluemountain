#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from tornado.routing import URLSpec as url

from sites.www.handlers import main
from sites.www.handlers import web_logs
from sites.www.handlers import file_upload
from sites.www.handlers import users

handlers = [
    url(r"/", main.IndexPageHandler),
    url(r"/web-logs", web_logs.WebLogsHandler),
    url(r"/web-log", web_logs.WebLogHandler),

    url(r"/file-upload", file_upload.FileUploadHandler),
    url(r"/files", file_upload.FilesHandler),
    url(r"/files/(\d+)", file_upload.FilesHandler),

    url(r"/users", users.UsersHandler)
]
