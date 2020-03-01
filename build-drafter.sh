#!/bin/bash
set -e -x

wget https://github.com/apiaryio/drafter/releases/download/v3.2.7/drafter-v3.2.7.tar.gz
tar xvzf drafter-v3.2.7.tar.gz
cd drafter-v3.2.7
python2 configure --shared
make libdrafter
cd ..
mkdir -p apiblueprint_view/lib
cp drafter-v3.2.7/build/out/Release/lib.target/libdrafter.so ./apiblueprint_view/lib/libdrafter.so
rm -rf drafter-v3.2.7/
rm drafter-v3.2.7.tar.gz
