#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

from setuptools import find_packages, setup

VERSION = '0.1'

setup(
    name="redfish",
    version='0.1',
    packages=find_packages(),
#    package_data={'models': 'models.py'},
    author='Benjamin',
    author_email='contact@blawesom.com',
    description="https://github.com/blawesom/niceredfish",
    url="http://redfish.blawesom.com/",
    entry_points={
        'console_scripts': [
            'redfish = redfish.redfish',
        ]
    },
    install_requires=[
        'setuptools',
        'Flask==1.0.2',
        'SQLAlchemy==1.2.15',
    ],
)