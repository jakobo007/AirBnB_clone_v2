#!/usr/bin/python3
"""Imported Modules"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a tgz archive for web_static"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    """generate archive name with date and time"""
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    archive_path = "versions/{}".format(archive_name)

    """create archive"""
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
