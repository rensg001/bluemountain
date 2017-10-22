#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
class File(object):
    """文件实体"""

    def __init__(
            self,
            file_id,
            name,
            type_,
            size,
            path,
            is_valid,
            create_time
    ):
       self.file_id = file_id
       self.name = name
       self.type_ = type_
       self.size = size
       self.path = path
       self.is_valid = is_valid
       self.create_time = create_time