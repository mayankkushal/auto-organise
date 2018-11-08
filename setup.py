#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'Organise'
DESCRIPTION = 'A little tool that helps you organise your directory into meaningful subdirectories.'
URL = 'https://github.com/mayankkushal/auto-organise'
EMAIL = 'mayankkushal26@gmail.com'
AUTHOR = 'Mayank Kushal'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = "0.3.0"

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

from distutils.core import setup

setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        organise=scripts.organise:cli
    ''',
)
