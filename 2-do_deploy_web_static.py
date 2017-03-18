#!/usr/bin/python3
from fabric.api import *
from time import strftime
import os.path

env.hosts = ['54.164.149.121', '52.201.184.69']


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
    """Deploy archive to servers."""
    if not os.path.exists(archive_path):
        print("File doesn't exist.")
        return False
    try:
        basename = os.path.basename(archive_path)
        archive_name = os.path.splitext(basename)[0]
        put("{}".format(archive_path), "/tmp/{}".format(basename))
        run("mkdir -p /data/web_static/releases/{}".format(archive_name))
        with cd("/data/web_static/releases"):
            run("tar -xzf /tmp/{} -C {}".format(basename, archive_name))
            run("rm /tmp/{}".format(basename))
            run("mv {}/web_static/* {}".format(archive_name, archive_name))
            run("rm -rf {}/web_static".format(archive_name))
            run("rm -rf ../current")
            run("ln -s {} ../current".format(archive_name))
        print("New version deployed!")
    except Exception as e:
        print("Error: {}\nUnable to deploy new version.".format(e))
        return False
