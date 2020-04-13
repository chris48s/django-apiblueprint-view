#!/bin/bash
set -e -x

DRAFTER_DIR="v4.1.0"
DRAFTER_VERSION="4.1.0"

wget https://github.com/apiaryio/drafter/releases/download/${DRAFTER_DIR}/drafter-${DRAFTER_VERSION}.tar.gz
tar xvzf drafter-${DRAFTER_VERSION}.tar.gz
cd drafter-${DRAFTER_VERSION}
mkdir build
cd build
cmake ..
make
cd ../..
mkdir -p apiblueprint_view/lib
cp drafter-${DRAFTER_VERSION}/build/src/libdrafter.so ./apiblueprint_view/lib/libdrafter.so
rm -rf drafter-${DRAFTER_VERSION}/
rm drafter-${DRAFTER_VERSION}.tar.gz
