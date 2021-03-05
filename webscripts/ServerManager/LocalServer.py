#!/bin/python3
from flask import render_template
from lib.server_info import *


def load_page():
    cpu = get_processor()
    ram = get_total_ram()
    disk = disk_total_space('/')

    return render_template('LocalServer.html',cpu=cpu,ram=ram,disk=disk)
