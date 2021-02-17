from shutil import copyfile
import socket
import struct
import fcntl
import os


def get_hostname():
    return socket.gethostname()


def set_hostname(hostname):
    print('set_hostname()[ hostname:', hostname, ']')
    os.system('hostnamectl set-hostname '+hostname)
    os.system('hostname '+hostname)


def enable_timedatectl_ntp(status=True):
    print('enable_timedatectl_ntp()[ status:', status, ']')
    if status:
        os.system('timedatectl set-ntp true')
    else:
        os.system('timedatectl set-ntp false')


def remove_smbconf():
    print('remove_smbconf()[]')
    smb_conf_file = "/etc/samba/smb.conf"
    if os.path.exists(smb_conf_file):
        os.remove(smb_conf_file)
    else:
        print(smb_conf_file, ' not exist')


def add_to_hosts(ip, domain, host):
    print('add_to_hosts()[ ip: ', ip, ' , domain: ',
          domain, ' ,host: ', host, ']')
    hosts = open("/etc/hosts", "a")
    hosts.write("\n# SADW\n")
    hosts.write(ip+'\t'+domain+'\t'+host)
    hosts.close()


def get_domain_from_realm(realm, hostname):
    domains = realm.split('.')

    if domains[0] != hostname:
        return domains[0]
    return domains[1]


def setup_domain(dc, dns_backend, realm, host, password):
    domain = get_domain_from_realm(realm, host)

    print('setup_domain()[ dc: ', dc, ' , dns_backend: ',
          dns_backend, ' , domain: ', realm, ' , host: ', host, ' , password: ', password, ']')
    os.system('samba-tool domain provision --server-role='+dc+' --use-rfc2307 --dns-backend='+dns_backend+' --realm=' +
              realm+' --domain='+domain+' --adminpass='+password)


def remove_resolvconf():
    print('remove_resolvconf()[]')
    conf = "/etc/resolv.conf"
    if os.path.exists(conf):
        os.remove(conf)
    else:
        print(conf, ' not exist')


def enable_samba_krb5():
    print('enable_samba_krb5()[]')
    copyfile('/var/lib/samba/private/krb5.conf', '/etc/samba/krb5.conf')


def add_self_to_resolv():
    print('add_self_to_resolv()[]')
    resolv = open("/etc/resolv.conf", "w")
    resolv.write('nameserver 127.0.0.1')
    resolv.close()


def disable_sharing_and_dns_services():
    print('disable_sharing_and_dns_services()[]')
    os.system('systemctl disable --now smbd nmbd winbind systemd-resolved')


def start_presistant_samba_ad_dc():
    print('start_presistant_samba_ad_dc()[]')
    os.system('systemctl unmask samba-ad-dc')
    os.system('systemctl enable --now samba-ad-dc')


def dns_samba_create_zone(ip, domain, password):
    ip_numbers = ip.split('.')
    pi = ip_numbers[2]+'.'+ip_numbers[1]+'.'+ip_numbers[0]

    command = 'samba-tool dns zonecreate '+ip + ' '+pi + \
        '.in-addr.arpa -Uadministrator@'+domain+' --password='+password
    print(command)
    os.system(command)


def install_pip():
    os.system('apt install python3-pip -y')
    return True


def pip_install_requirements():
    os.system('pip3 install -r requirements.txt')
