from pyroute2 import IPDB  # https://docs.pyroute2.org
import socket


def get_IP():
    # TODO use pyroute2 in get_IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('1.1.1.1', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


def set_IP(iface, ip, mask='24'):
    # TODO use iface
    ipdb = IPDB()
    with ipdb.interfaces.enp0s3 as enp0s3:
        enp0s3.add_ip(ip+'/'+mask)
    ipdb.release()
