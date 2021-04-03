#!/bin/sh
# Install python3 and python3-pip
sudo apt-get install -y python3 python3-pip

# Download docker install commands from the web, run this as a bash script
curl https://get.docker.com | sudo bash

# Add the current user docker users
sudo groupadd docker
sudo usermod -aG docker $(whoami)
sudo chmod 777 /var/run/docker.sock

# Install jq & curl
sudo apt update
sudo apt install -y curl jq

# Install latest version of docker-compose
version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')

# Download the latest compose file to /usr/local/bin/docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Change permissions to make file executable
sudo chmod +x /usr/local/bin/docker-compose

# Create a link to docker-compose in our path
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# Check if installed
docker-compose --version