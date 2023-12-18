#!/usr/bin/env bash
# Script that sets up two web servers web_static deployment

# Install nginx if not exist
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

# Create folders
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir /data/web_static/releases/test/

# Create a fake HTML FILE for testing nginx
sudo echo "<html>
  <head>
  </head>
  <body>
  Holberton School
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to point to /data/web_static/releases/test/
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ ->'recursively' to user:group
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration to serve the content of/data/web_static/current/
# to hbnb_static (  ex: https://mydomainname.tech/hbnb_static)
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart server nginx
sudo service nginx restart
