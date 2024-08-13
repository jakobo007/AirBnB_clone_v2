#!/usr/bin/python3
"""Imported Modules"""
from fabric.api import env
from os.path import exists
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['100.26.227.224', '34.227.92.200']


def deploy():
    """Creates and distributes archive to web servers"""

    """Create archive"""
    archive_path = do_pack()
    if archive_path is None or not exists(archive_path):
        return False

    """Deploy archive"""
    return do_deploy(archive_path)
