#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os

debug = True
template_dir = "templates"
static_dir = "static"

login_url = "/users"
cookie_secret = "95388bfc-e6c0-4c7e-8ed0-ee7437c49581"

mysql = "mysql+mysqlconnector://root:123456@localhost:3306/bluemountain"

cur_dir = os.path.dirname(os.path.realpath(__file__))
upload_path = os.path.join(os.path.dirname(cur_dir), "uploads")