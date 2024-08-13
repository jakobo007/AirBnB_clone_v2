#!/usr/bin/python3
"""Imported Modules"""
from fabric.api import env
from os.path import exists
import importlib.util

# Dynamically import 1-pack_web_static
pack_spec = importlib.util.spec_from_file_location("pack_web_static", "1-pack_web_static.py")
pack_web_static = importlib.util.module_from_spec(pack_spec)
pack_spec.loader.exec_module(pack_web_static)

# Dynamically import 2-do_deploy_web_static
deploy_spec = importlib.util.spec_from_file_location("do_deploy_web_static", "2-do_deploy_web_static.py")
do_deploy_web_static = importlib.util.module_from_spec(deploy_spec)
deploy_spec.loader.exec_module(do_deploy_web_static)

env.hosts = ['100.26.227.224', '34.227.92.200']


def deploy():
    """Creates and distributes archive to web servers"""

    """Create archive"""
    archive_path = do_pack()
    if archive_path is None or not exists(archive_path):
        return False

    """Deploy archive"""
    return do_deploy(archive_path)
