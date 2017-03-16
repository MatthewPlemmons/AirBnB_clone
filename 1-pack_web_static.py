#!/usr/bin/python3
"""fabfile"""
from fabric.api import local
from datetime import datetime

def do_pack():
    local('mkdir -p versions')
    time = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
    archive = 'versions/web_static_{}.tgz'.format(time)
    try:
        local('tar -cvzf {} web_static'.format(archive))
    except:
        return None
    return archive
