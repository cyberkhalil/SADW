#!/bin/python3
from flask import Flask, render_template

from routes import routes

template_path = 'static/templates'

app = Flask(__name__,
            template_folder=template_path,  # static imgs/html/css
            static_folder='static')  # entire static


# the 'ServerManager' directory in server
sm_path = '/ServerManager'

from lib.manage_network import get_IP
from lib.server_info import (disk_total_space, get_ceip, get_error_reporting,
                             get_firewall_status, get_hostname,
                             get_last_checked_updates,
                             get_last_installed_updates, get_NICT_status,
                             get_osversion, get_peripheral_hw_info,
                             get_processor, get_rdp_status,
                             get_remote_management_status, get_server_dn,
                             get_time_zone, get_total_ram)


@app.route(sm_path+'/')
@app.route('/')
def Dashboard_page():
    return render_template('Dashboard.html')

@app.route(sm_path+'/LocalServer')
@app.route(sm_path+'/LocalServer.html')
def LocalServer_page():
    cpu = get_processor()
    ram = get_total_ram()
    disk = disk_total_space('/')
    hostname = get_hostname()
    ipaddress= get_IP('wlo1')
    osversion = get_osversion()
    timezone= get_time_zone()
    server_dn = get_server_dn()
    firewall_status = get_firewall_status()
    nict_status = get_NICT_status()
    rdp_status = get_rdp_status()
    rm_status = get_remote_management_status()
    ceip_status = get_ceip()
    error_reporting_status=get_error_reporting()
    li_updates=str(get_last_installed_updates())
    lc_updates=str(get_last_checked_updates())
    hw_information = get_peripheral_hw_info()

    return render_template('LocalServer.html',cpu=cpu,ram=ram,disk=disk,hostname=hostname,ip=ipaddress,osversion=osversion,timezone=timezone,server_dn=server_dn,firewall_status=firewall_status,nict_status=nict_status,rdp_status=rdp_status,rm_status=rm_status,ceip_status=ceip_status,error_reporting_status=error_reporting_status,li_updates=li_updates,lc_updates=lc_updates,hw_information=hw_information)

routes.template_route(app,sm_path,template_path)

if __name__ == '__main__':
    app.run(debug=True)
