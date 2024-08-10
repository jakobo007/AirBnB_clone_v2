#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install nginx -y

# make directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_statict/shared/

# create files
echo "
<html>
<head></head>
<body>
Hello Holberton
</body>
</html>
" | sudo tee /data/web_static/releasses/test/index.html

# create symbol link
sudo ln -f /data/web_static/releases/test/ /data/web_static/current

# give ownership
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" $nginx_config; then
    sudo sed -i '/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $nginx_config
fi

# Restart Nginx to apply changes
sudo service nginx restart

echo "Web server setup completed successfully
