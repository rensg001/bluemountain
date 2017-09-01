#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sites.services.logs.entity import Log
from .model import LogsModel
from ..base import Session


def create(log: Log) -> int:
    log = LogsModel(
        id=log.id_,
        content=log.content,
        create_date=log.create_date,
        create_time=log.create_time,
        update_time=log.update_time,
        is_valid=log.is_valid or True
    )
    with Session() as session:
        session.add(log)
        session.commit()
        log_id = log.id

    return log_id
