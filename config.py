#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   config.py
@Time    :   2024/01/25 21:08:44
@Author  :   lvguanjun
@Desc    :   config.py
"""

import yaml

with open("setting.yaml", "r") as f:
    settings = yaml.load(f, Loader=yaml.FullLoader)

host = "127.0.0.1"
port = 5000

username = settings["username"]
password = settings["password"]
root_dir = settings["root_dir"]

host = settings.get("host", host)
port = settings.get("port", port)
