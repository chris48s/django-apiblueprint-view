#!/bin/sh
set -e

yum install -y wget
/opt/python/cp36-cp36m/bin/pip install poetry
./build-drafter.sh
/opt/python/cp36-cp36m/bin/poetry install
/opt/python/cp36-cp36m/bin/poetry build -f wheel

for whl in ./dist/*.whl; do
  auditwheel repair $whl --plat "manylinux1_x86_64" -w ./dist
done

/opt/python/cp36-cp36m/bin/poetry config pypi-token.pypi "$1"
/opt/python/cp36-cp36m/bin/poetry publish -vvv -n
