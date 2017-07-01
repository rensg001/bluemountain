#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""站点程序入口"""
import os

import jinja2

from tornado.ioloop import IOLoop
from tornado.routing import URLSpec
from tornado.web import Application
from tornado.httpserver import HTTPServer

from tornado.web import RequestHandler
from tornado_jinja2 import Jinja2Loader


class IndexPageHandler(RequestHandler):
    """网站主页"""

    def get(self):
        return self.render("index.html")


def main():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(cur_dir, "templates")
    # Create a instance of Jinja2Loader
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_path),
        autoescape=False,
    )
    jinja2_loader = Jinja2Loader(jinja2_env)

    # Give it to Tornado to replace the default Loader.
    settings = dict(template_loader=jinja2_loader, debug=True)
    app = Application([URLSpec(r"/", IndexPageHandler)], **settings)
    server = HTTPServer(app)
    server.listen(8888)
    IOLoop.current().start()

if __name__ == "__main__":
    main()
