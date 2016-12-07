#!/bin/bash

apt-get update

# Python
apt-get install python2 -y
apt-get install python-dev -y
apt-get install python-pip -y

# Flask
pip install flask==0.10.1

# Boto
pip install boto==2.32.1

# ZeroMQ
apt-get install libzmq3=3.2.3+dfsg-2 -y
apt-get install libzmq-dev=3.2.3+dfsg-2 -y
pip install pyzmq==14.3.1

# Misc
pip install python-dateutil==2.2
pip install tldextract==1.4