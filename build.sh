#!/bin/bash

# Update and install system packages required to build dlib
apt-get update && apt-get install -y cmake g++ python3-dev
pip install distutils

# Install Python packages
pip install -r requirements.txt
