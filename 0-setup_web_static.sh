#!/usr/bin/env bash
# A bash script that sets up web server for deployment of web_static.

WEBSTATIC="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Creates the directories if they do not exist.
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Creates a fake HTML file to test Nginx configuration.
echo "The HTML file tests the Nginx Configuration" | sudo tee /data/web_static/releases/test/index.html

# Creates a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gives ownership of the /data/ folder to the ubuntu user AND group, recursively.
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "35i $WEBSTATIC" /etc/nginx/sites-available/default
sudo service nginx start
