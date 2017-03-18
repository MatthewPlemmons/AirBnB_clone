#!/usr/bin/python3
from fabric.api import local
from time import strftime


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
