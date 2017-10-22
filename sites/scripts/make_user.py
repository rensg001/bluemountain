#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import argparse

from sites.services.users import users


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("username")
    ap.add_argument("password")
    args = ap.parse_args()
    users.create(args.username, args.password)


if __name__ == "__main__":
    main()
