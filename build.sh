#!/bin/bash
apt-get update && apt-get install -y cmake g++ python3-dev python3-distutils
pip install --upgrade pip
pip install -r requirements.txt
