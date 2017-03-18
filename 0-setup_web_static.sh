#!/usr/bin/env bash
# Sets up nginx and directories to serve files from.
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "TESTING" > /data/web_static/releases/test/index.html
ln -fs /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

config="server {
    location /hbnb_static/ {
	alias /data/web_static/current/;
    }
}"

echo "$config" > /etc/nginx/sites-available/default
service nginx restart
