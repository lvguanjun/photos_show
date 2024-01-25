#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2024/01/25 21:08:39
@Author  :   lvguanjun
@Desc    :   main.py
"""

import os
import subprocess

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash, generate_password_hash

from config import host, password, port, root_dir, username

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {username: generate_password_hash(password)}


@app.route("/api/images")
def get_images():
    result = subprocess.run(["ls", root_dir], capture_output=True, text=True)
    images = result.stdout.splitlines()
    return jsonify(images)


@app.route("/api/images/<filename>", methods=["DELETE"])
@auth.login_required
def delete_image(filename):
    os.remove(os.path.join(root_dir, filename))
    return "", 204


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


if __name__ == "__main__":
    app.run(host=host, port=port)
