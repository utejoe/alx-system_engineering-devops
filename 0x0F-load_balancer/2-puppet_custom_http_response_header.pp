#!/usr/bin/env bash
# Script that configures Nginx server with a custom header
apt-get -y update
apt-get -y install nginx
echo "Hello World!" > /var/www/html/index.nginx-debian.html
echo "Ceci n'est pas une page" > /usr/share/nginx/html/custom_404.html
sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/AyBims permanent;\n\n\terror_page 404 \/custom_404.html;\n\tlocation = \/custom_404.html {\n\t\troot \/usr\/share\/nginx\/html;\n\t\tinternal;\n\t}/" /etc/nginx/sites-available/default
sed -i "s/include \/etc\/nginx\/sites-enabled\/\;/include \/etc\/nginx\/sites-enabled\/\;\n\tadd_header X-Served-By \"$HOSTNAME\";/" /etc/nginx/nginx.conf
service nginx start
