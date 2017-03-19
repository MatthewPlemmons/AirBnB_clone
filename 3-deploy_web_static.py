#!/usr/bin/python3
from fabric.api import *
from time import strftime
import os.path

env.hosts = ['107.20.68.230:34181']
env.user = 'root'


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
        sudo("mkdir -p /data/web_static/releases/{}".format(archive_name))
        data_dir = '/data/web_static/releases'
        sudo("tar -xzf /tmp/{} -C {}/{}".format(basename, data_dir, archive_name))
        sudo("rm /tmp/{}".format(basename))
        sudo("mv {}/{}/web_static/* {}/{}".format(data_dir, archive_name, data_dir, archive_name))
        sudo("rm -rf {}/{}/web_static".format(data_dir, archive_name))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/{}/ /data/web_static/current".format(data_dir, archive_name))
        print("New version deployed!")
        return True
    except Exception as e:
        print("Error: {}\nUnable to deploy new version.".format(e))
        return False


def deploy():
    try:
        archive = do_pack()
        result = do_deploy(archive)
        return result
    except:
        return False
