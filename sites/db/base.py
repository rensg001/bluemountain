#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tornado.options import options

engine = create_engine(options.mysql, echo=True)

OriginSession = sessionmaker(bind=engine)


class Session(object):
    def __init__(self):
        self.origin_session = OriginSession()

    def __enter__(self):
        return self.origin_session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.origin_session.close()


ModelBase = declarative_base()
