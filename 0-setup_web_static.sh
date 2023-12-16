#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static.
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
webpage="<html>
  <head>
  </head>
  <body>
    HBNB PAGE
  </body>
</html>" 
echo "$webpage" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart
exit 0
