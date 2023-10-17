#!/bin/bash

set -euxo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 [mac|linux]"
    exit 1
fi

platform="$1"

wget https://github.com/apiaryio/drafter/releases/download/v3.2.7/drafter-v3.2.7.tar.gz
tar xvzf drafter-v3.2.7.tar.gz
cd drafter-v3.2.7
python2.7 configure --shared
make libdrafter
cd ..
mkdir -p apiblueprint_view/lib
if [ "$platform" = "mac" ]; then
    cp drafter-v3.2.7/build/out/Release/libdrafter.dylib ./apiblueprint_view/lib/libdrafter.dylib
else
    cp drafter-v3.2.7/build/out/Release/lib.target/libdrafter.so ./apiblueprint_view/lib/libdrafter.so
fi
rm -rf drafter-v3.2.7/
rm drafter-v3.2.7.tar.gz
