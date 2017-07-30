import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-apiblueprint-view',
    author="chris48s",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'draughtsman',
        'django-markdown-deux',
    ]
)
