import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

def _get_description():
    try:
        path = os.path.join(os.path.dirname(__file__), 'README.rst')
        with open(path, encoding='utf-8') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name='django-apiblueprint-view',
    version='1.1.2',
    author="chris48s",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    description='Render API Blueprints on-the-fly using Django templates',
    long_description=_get_description(),
    url='https://github.com/chris48s/django-apiblueprint-view',
    install_requires=[
        'draughtsman',
        'markdown2',
        'typing',
    ],
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
