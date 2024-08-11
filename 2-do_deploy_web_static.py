#!/usr/bin/python3
from fabric.api import env, put, run
import os

# Define the IPs of your web servers
env.hosts = ['<IP web-01>', '<IP web-02>']

def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    
    # Check if the archive path exists
    if not os.path.exists(archive_path):
        return False
    
    # Extract the archive filename and folder name
    archive_filename = os.path.basename(archive_path)
    archive_folder = archive_filename.replace('.tgz', '')
    release_folder = "/data/web_static/releases/{}/".format(archive_folder)
    
    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")
        
        # Uncompress the archive to the release folder
        run("mkdir -p {}".format(release_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))
        
        # Move the files out of the extracted folder to the release folder
        run("mv {0}web_static/* {0}".format(release_folder))
        run("rm -rf {}web_static".format(release_folder))
        
        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))
        
        # Delete the current symbolic link
        run("rm -rf /data/web_static/current")
        
        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_folder))
        
        return True
    except:
        return False
