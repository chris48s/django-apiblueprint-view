#!/bin/bash

set -euxo pipefail

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt install python2.7
