#!/bin/python3
import os
from lib import manage_distro, util

# update distro
manage_distro.update()

# install pip
util.install_pip()

# install requirements
util.pip_install_requirements()

# install dependencies
manage_distro.install_deps()

# run install script
os.system('python3 install.py')
