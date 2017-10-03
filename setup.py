import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-apiblueprint-view',
    version='1.1.0',
    author="chris48s",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    description='Render API Blueprints on-the-fly using Django templates',
    url='https://github.com/chris48s/django-apiblueprint-view',
    install_requires=[
        'draughtsman',
        'markdown2',
        'typing',
    ]
)
