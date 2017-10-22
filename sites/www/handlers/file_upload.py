#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""文件上传模块"""
import sys

from tornado.web import authenticated

from sites.www.handlers.handler import BaseHandler
from sites.www.handlers.handler import ResponseResult
from sites.services.file_upload import file_upload


class FileUploadHandler(BaseHandler):
    """文件上传"""

    @authenticated
    def get(self):
        return self.render("file-upload/file-upload.html")

    def post(self):
        upload_file = self.request.files["file-upload"][0]
        data = {
            "file_name": upload_file.filename,
            "size": sys.getsizeof(upload_file.body),
            "content_type": upload_file.content_type,
            "content": upload_file.body
        }
        file_upload.create(
            name=data["file_name"],
            size=data["size"],
            content_type=data["content_type"],
            content=data["content"]
        )
        self.write(ResponseResult())
        self.finish()
        return


class FilesHandler(BaseHandler):
    """文件列表"""

    @authenticated
    def get(self, file_id=None):
        action = self.get_argument("action", default="")
        if action == "all":
            all_files = file_upload.get_all()
            self.write(all_files)
            self.set_header("Content-Type", "application/json;charset=UTF-8")
            self.finish()
            return
        elif action == "download":
            try:
                file_id = int(file_id)
            except TypeError:
                self.write_error(400)
                return

            file_info = file_upload.get_one(file_id)
            self.set_header("Content-Type", "application/octet-stream")
            self.set_header(
                "Content-Disposition",
                b"attachment; filename=" + file_info.name.encode("utf-8")
            )
            chunk_size = 4096
            with open(file_info.real_path, mode="rb") as f:
                while True:
                    data = f.read(chunk_size)
                    if not data:
                        break
                    self.write(data)

            self.finish()
            return

        return self.render("file-upload/files.html")
