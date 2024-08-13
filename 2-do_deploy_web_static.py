#!/usr/bin/python3
"""Imported Modules"""
from fabric.api import env, put, run
import os

env.hosts = ['100.26.227.224', '34.227.92.200']


def do_deploy(archive_path):
    """Deploys archive to server"""
    if not os.path.exists(archive_path):
        return False

    """Extract file information"""
    file_name = os.path.basename(archive_path)
    no_ext = file_name.split('.')[0]
    release_dir = "/data/web_static/releases/{}/".format(no_ext)
    try:

        """Upload the archive"""
        put(archive_path, "/tmp/")

        """Uncompress the archive"""
        run("sudo mkdir -p {}".format(release_dir))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, release_dir))

        """remove archive"""
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}web_static/* {}".format(release_dir, release_dir))
        run("sudo rm -rf {}web_static".format(release_dir))

        """Update the symbolic link"""
        run("sudo rm -fr /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(release_dir))
        return True

    except Exception as e:
        print("Deployment failed: ", e)
        return False
