#!/bin/python3
import socket
import struct
import fcntl
import os


def get_hostname():
    return socket.gethostname()

def set_hostname(hostname):
    os.system('hostnamectl set-hostname '+hostname)
    os.system('hostname '+hostname)


def get_IP():
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

def set_IP(iface, ip):
    SIOCSIFADDR = 0x8916
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bin_ip = socket.inet_aton(ip)
    ifreq = struct.pack('16sH2s4s8s', iface, socket.AF_INET,
                        (b'\x00' * 2), bin_ip, (b'\x00' * 8))
    fcntl.ioctl(sock, SIOCSIFADDR, ifreq)


def enable_timedatactl_ntp(status=True):
    if status:
        os.system('timedatactl set-ntp true')
    else:
        os.system('timedatactl set-ntp false')

