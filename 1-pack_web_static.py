#!/usr/bin/python3
"""Module contains function that compresses web_static folder
"""

from datetime import date
from time import strftime
from fabric.api import local
import os


def do_pack():
    """Function to compress web_static folder"""
    file_time = strftime("%Y%m%d%H%M%S")

    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        command = "tar -cvzf"
        compressed = "versions/web_static_{}.tgz".format(file_time)
        target = "web_static/"
        local('{} {} {}'.format(command, compressed, target))
        return compressed
    except Exception as e:
        return None
