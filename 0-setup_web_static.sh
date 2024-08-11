#!/usr/bin/env bash
# setup web servers to deploy web static
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

# make directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

# create index file
sudo echo "<html>
<head>
<body>
Holberton School
</body>
</head>
</html>" | sudo tee /data/web_static/releases/index.html

# create symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/server_name _;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart