#!/bin/sh
/usr/bin/lsb_release -a
add-apt-repository universe
sudo apt-get update
apt-get install -y  python3-venv
