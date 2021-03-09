
from pyroute2 import IPRoute

def set_IP(iface,ip,mask):
    ip = IPRoute()
    index = ip.link_lookup(ifname=iface)[0]
    ip.addr('add', index, address=ip, mask=mask)
    ip.close()

set_IP('wlo1','192.168.1.112',24)

