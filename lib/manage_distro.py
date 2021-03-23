#!/bin/python3
# TODO make it distro generic
import os

import distro


def update():
    os.system('apt update -y')
    return True

def upgrade():
    os.system('apt full-upgrade -y')
    return True

def install_deps():
    os.system('apt install samba krb5-config winbind smbclient -y')
    return True

def get_update_log_files():
    import subprocess
    proc = subprocess.Popen(["ls /var/log/dpkg.log*"], 
    stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
    result = proc.stdout.read().decode("utf-8")
    return result.splitlines() if "cannot access" not in result else []

def get_check_update_log_file():
    return "/var/lib/apt/periodic/update-success-stamp"

