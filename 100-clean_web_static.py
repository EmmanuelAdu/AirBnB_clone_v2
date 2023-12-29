#!/usr/bin/python3
"""This script deletes out-of-date archive files from versions/
dir
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""
import os
from fabric.api import *


env.hosts = ['35.153.18.211', '34.207.222.234']


def do_clean(number=0):
    """Function to delete archive files
    Arg:
        number (int) - number of archives to delete
    When 0 or 1 keep most recent version of archive
    When 2 keep most recent and 2-most recent
    """
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(files)) for files in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
