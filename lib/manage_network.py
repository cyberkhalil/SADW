import socket

import psutil


def get_interfaces():
    import netifaces
    return netifaces.interfaces()

'''
another wat yo get interfaces
def getAllInterfaces():
    return os.listdir('/sys/class/net/')
'''

def iface_isup(iface):
    return psutil.net_if_stats()[iface][0]

def get_IP(iface='enp0s3'):
    return psutil.net_if_addrs()[iface][0][1]


# check if valid ip in network

def is_in_network(ip,network):
    import ipaddress
    if not(is_valid_ipv6_address(ip)) and not(is_valid_ipv4_address(ip)):
        return "invalid address"
    net = ipaddress.ip_network(network)
    ip = ipaddress.ip_address(ip)
    return ip in net


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
'''
TODO: set ip

def set_IP(iface, ip, mask='24'):
    from pyroute2 import IPDB
    # TODO use iface
    ipdb = IPDB()
    with ipdb.interfaces.enp0s3 as enp0s3:
        ipdb.interfaces.enp0s3.add_ip(ip+'/'+mask)
    ipdb.release()
'''


def set_IP(ifname='enp0s3',address='172.24.6.88',mask=16):
    from pyroute2 import IPRoute
    ip = IPRoute()
    index = ip.link_lookup(ifname=ifname)[0]
    ip.addr('add', index, address=address, mask=mask)
    ip.close()

"""
## Testing 
print(get_IP())
"""
