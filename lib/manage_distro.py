# TODO make it distro generic
import distro
import os


def update():
    os.system('apt update -y')
    return True


def upgrade():
    os.system('apt full-upgrade -y')
    return True


def install_deps():
    os.system('apt install samba krb5-config winbind smbclient -y')
    return True
