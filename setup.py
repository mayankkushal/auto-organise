#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os, errno
import sys
from shutil import rmtree, copyfile

from setuptools import find_packages, setup, Command
from setuptools.command.install import install


class PostInstallCommand(install):
    """Copies the nautilus_gui.py to the correct location"""

    def make_and_copy(self):
        extension_dir = ".local/share/nautilus-python/extensions"
        user = os.path.expanduser("~")
        final_dir = os.path.join(user, extension_dir)
        nautilus_dir = os.path.join(user, '.local/share/nautilus-python')
        try:
            os.makedirs(final_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        current = os.path.dirname(os.path.realpath(__file__))
        py_path = os.path.join(current, 'scripts/nautilus_gui.py')
        copyfile(py_path, final_dir+'/nautilus_gui.py')

        # Assign permissions
        os.system("sudo chmod 777 "+nautilus_dir)
        os.system("sudo chmod 777 "+final_dir)
        os.system("sudo chmod 777 "+final_dir+'/nautilus_gui.py')

    def run(self):
        install.run(self)
        self.make_and_copy()
        print("Install Successfull")
        value = input("Nautilus needs to be restarted for all the changes to take affect. Restart now? [Y/n]: ")
        if value=='Y' or value=="y":
            print("Restarting...")
            os.system("killall nautilus")



# Package meta-data.
NAME = 'Organise'
DESCRIPTION = 'A little tool that helps you organise your directory into meaningful subdirectories.'
URL = 'https://github.com/mayankkushal/auto-organise'
EMAIL = 'mayankkushal26@gmail.com'
AUTHOR = 'Mayank Kushal'
REQUIRES_PYTHON = '>=3.5.0'
VERSION = "2.0.0"

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
    author=AUTHOR,
    author_email=EMAIL,
    url='https://github.com/mayankkushal/auto-organise',
    description=DESCRIPTION,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=[
        'Click', 'tqdm'
    ],
    entry_points='''
        [console_scripts]
        organise=scripts.organise:cli
    ''',
    cmdclass={
        'install': PostInstallCommand,
    },
)
