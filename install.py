#!/bin/python3
from lib import manage_distro, manage_network, util

ip = input('Enter your static ip ['+manage_network.get_IP()+']:')
if not ip:
    ip = manage_network.get_IP()
manage_network.set_IP('enp0s3', ip,24)

host = input('Enter host name ['+util.get_hostname()+']:')
if not host:
    host = util.get_hostname()

domain = input('Enter your domain ['+host+'.example.com]:')
if not domain:
    domain = host+'.example.com'
util.set_hostname(domain)

# enable ntp
util.enable_timedatectl_ntp()

# add domain to hosts
util.add_to_hosts(ip, domain, host)

# remvoe obselete samba conf
util.remove_smbconf()

# input admin password
password = input('Enter admin password [or Passw0rd]')
if not password:
    password = 'Passw0rd'

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
