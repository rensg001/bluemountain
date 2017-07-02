#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""网站主页"""

from sites.www.handlers.handler import BaseHandler


class IndexPageHandler(BaseHandler):
    """网站主页"""

    def get(self):
        return self.render("index.html")
