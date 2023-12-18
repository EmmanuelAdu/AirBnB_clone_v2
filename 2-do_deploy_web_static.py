#!/usr/bin/python3
"""Script distributes an archive to web servers
"""
import os
from fabric.api import put, run, env

env.hosts = ['35.153.18.211', '34.207.222.234']


def do_deploy(archive_path):
    """Function to send archived file to web server
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    name, ext = os.path.splitext(file_name)
    tmp_path = "/tmp/{}".format(file_name)
    new_path = "/data/web_static/releases/{}".format(name)

    try:
        put(archive_path, tmp_path)
        run("mkdir -p {}".format(new_path))
        run("tar -xzf {} -C {}".format(tmp_path, new_path))
        run("rm {}".format(tmp_path))
        run("mv {}/web_static/* {}/".format(new_path, new_path))
        run("rm -rf {}/web_static".format(new_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_path))
        return True
    except:
        return False
