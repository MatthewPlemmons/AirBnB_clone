#!/usr/bin/python3
from fabric.api import local
from time import strftime
import os.path

def do_pack():
    """Archive the web_static directory."""
    try:
        local('mkdir -p versions')
        current_time = strftime('%Y%m%d%H%M%S')
        archive_name = 'versions/web_static_{}.tgz'.format(current_time)
        local('tar -cvzf {} web_static'.format(archive_name))
        return archive_name
    except:
        return None

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False
    try:
        put("version/{}".format(archive_path), "/tmp/{}".format(archive_path))
        basename = os.path.basename(archive_path)
        archive_name = os.path.splitext(basename)[0]
        run("mkdir -p /data/web_static/releases/{}".format(archive_name))

        # Unzip file into correct directory.
        run("tar -xzf /tmp/{}"
