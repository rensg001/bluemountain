#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class Log(object):
    """日志实体"""

    def __init__(self,
                 id_,
                 content,
                 create_date,
                 create_time,
                 update_time,
                 is_valid):
        self.id_ = id_
        self.content = content
        self.create_date = create_date
        self.create_time = create_time
        self.update_time = update_time
        self.is_valid = is_valid
