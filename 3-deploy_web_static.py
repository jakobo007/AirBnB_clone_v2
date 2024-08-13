#!/usr/bin/python3
"""Imported Modules"""
from fabric.api import env, put, run, local
from os.path import exists
from datetime import datetime
import os

env.hosts = ['100.26.227.224', '34.227.92.200']


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

def deploy():
    """Creates and distributes archive to web servers"""

    """Create archive"""
    archive_path = do_pack()
    if archive_path is None or not exists(archive_path):
        return False

    """Deploy archive"""
    return do_deploy(archive_path)
