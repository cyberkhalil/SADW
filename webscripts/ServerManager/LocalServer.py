#!/bin/python3
from flask import render_template
from lib.manage_network import *
from lib.server_info import *
from lib.util import *


def load_page():
    cpu = get_processor()
    ram = get_total_ram()
    disk = disk_total_space('/')
    hostname = get_hostname()
    ipaddress= get_IP('wlo1')
    osversion = get_osversion()
    timezone= get_time_zone()

    return render_template('LocalServer.html',cpu=cpu,ram=ram,disk=disk,hostname=hostname,ip=ipaddress,osversion=osversion,timezone=timezone)
