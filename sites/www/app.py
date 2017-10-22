#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""站点程序入口"""
import os

import jinja2

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado_jinja2 import Jinja2Loader
from tornado.log import gen_log
from tornado.log import enable_pretty_logging
from tornado.options import define

from sites.www import settings

# 定义模块命令行选项
define("template-dir", default="templates", help="模版根目录")
define("debug", default=True, help="是否开发模式")
define("static-dir", default="static", help="静态文件根目录")
define(
    "mysql",
    help="数据配置",
)


def main():
    enable_pretty_logging()
    gen_log.info("server is starting...")

    gen_log.info("read config.")
    cur_dir = os.path.dirname(os.path.abspath(__file__))

    # Create a instance of Jinja2Loader
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            os.path.join(cur_dir, settings.template_dir),
        ),
        autoescape=True,
    )
    jinja2_loader = Jinja2Loader(jinja2_env)

    # Give it to Tornado to replace the default Loader.
    configs = dict(template_loader=jinja2_loader,
                   debug=settings.debug,
                   static_path=settings.static_dir,
                   cookie_secret=settings.cookie_secret,
                   login_url=settings.login_url)

    from sites.www.routes import handlers
    app = Application(handlers=handlers, **configs)
    server = HTTPServer(app)
    server.listen(8888)
    gen_log.info("server started.")
    IOLoop.current().start()


if __name__ == "__main__":
    main()
