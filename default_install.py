#!/bin/python3
## pre install

from lib import manage_distro, util

# update distro
manage_distro.update()

# install pip
util.install_pip()

# install requirements
util.pip_install_requirements()

# install dependencies
manage_distro.install_deps()

## install
from lib import manage_distro, manage_network, util

ip = manage_network.get_IP()
host = util.get_hostname()
domain = host+'.example.com'
password = 'Passw0rd'

manage_network.set_IP('enp0s3', ip,24)

util.set_hostname(domain)

# enable ntp
util.enable_timedatectl_ntp()

# add domain to hosts
util.add_to_hosts(ip, domain, host)

# remvoe obselete samba conf
util.remove_smbconf()

# setup domain
util.setup_domain('dc', 'SAMBA_INTERNAL',
                  domain.upper(), host.upper(), password)

# remove resolv conf
util.remove_resolvconf()

# enable samba krb5
util.enable_samba_krb5()

# add self nameserver to resolv config
util.add_self_to_resolv()

# disable sharing and dns services
util.disable_sharing_and_dns_services()

# run and enable samba ad dc
util.start_presistant_samba_ad_dc()

# create zone in internal samba dns
util.dns_samba_create_zone(ip, domain, password)
