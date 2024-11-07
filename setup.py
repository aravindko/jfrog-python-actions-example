#!/usr/bin/env python

from setuptools import setup

setup(
    name='JFROG_py_POC',
    version='1.0',
    description='Project example for building Python project with JFrog products.',
    author='JFrog',
    author_email='ar_poc',
    url='https://github.com/',
    packages=['pythonExample'],
    install_requires=['PyYAML>3.11', 'nltk','urllib3==1.26.18'],
)
