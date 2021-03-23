from subprocess import PIPE, STDOUT, Popen

from psutil import cpu_percent, disk_partitions, disk_usage, virtual_memory

from lib.util import (fixstring, get_file_timestamp, get_hostname,
                      service_status)


def get_osversion():
    try:
        import platform
        return platform.platform()
    except:
        return "module platform not found"

def get_server_dn():
    try:
        proc = Popen(["samba-tool","computer","show",get_hostname()], stdout=PIPE)
        
        prefix = "dNSHostName: "
        suffix = "objectCategory:"

        out = fixstring(proc.communicate()[0],prefix,suffix)
        out = out[:-2]
        return out
    except:
        return "Not a DC"

def get_time_zone():
    try:
        import time
        return time.asctime(time.gmtime())
    except:
        return "module time not found"

def get_processor():
    try:
        from cpuinfo import get_cpu_info
        return get_cpu_info()['brand_raw']
    except:
        return "module cpuinfo not found"

def get_cpu_usage():
        cpu = cpu_percent(interval=1)
        return str(cpu) + "%"

def get_total_ram():
    return round(virtual_memory().total/(1024**3))
def get_used_ram():
    return round(virtual_memory().used/(1024**3))
def get_free_ram():
    return round(virtual_memory().free/(1024**3))

def disks_list():
    li =[]
    for disk in disk_partitions():
        li.append(disk[1])
    return li

def disk_total_space(disk_mountpoint):
    return round(disk_usage(disk_mountpoint).total/(1024**3))

def disk_used_space(disk_mountpoint):
    return round(disk_usage(disk_mountpoint).used/(1024**3))

def disk_free_space(disk_mountpoint):
    return round(disk_usage(disk_mountpoint).free/(1024**3))

def get_firewall_status():
    """ Will use firewalld as firewall service """
    firewall_service_name = "firewalld"
    status = service_status(firewall_service_name)
    return "On" if status == 1 else "Off"

def get_NICT_status():
    """ Not Supported yet"""
    return "Disabled"

def get_rdp_status():
    """ Not Supported yet"""
    return "Disabled"

def get_remote_management_status():
    """ Will use sshd as remote management service """
    remote_management_service_name = "sshd"
    status = service_status(remote_management_service_name)
    return "Enabled" if status == 1 else "Disabled"

def get_ceip():
    """ Not Supported yet
    Customer Experience Improvement Program is to send log
     to Microsoft to make a better experience for its customers, 
     we can do something like that to send us some logs but not now... 
     so it's disabled here """
    return "Not participating"

def get_error_reporting():
    """ Not Supported yet
    The error reporting feature enables users to notify Microsoft of
     application faults, kernel faults, unresponsive applications, 
     and other application specific problems. Microsoft can use the 
     error reporting feature to provide customers with troubleshooting 
     information, solutions, or updates for their specific problems. """
    return "Off"

def get_last_installed_updates():
    import datetime

    from lib.manage_distro import get_update_log_files
    update_log_files = get_update_log_files()
    
    datetime_list = []
    for log_file in update_log_files:
        f = open(log_file, "r")
        lines = f.readlines()
        if len(lines)==0:
            continue
        else:
            for line in lines:
                if "upgrade" in line:
                    splits = line.split(' ')
                    time_splits = splits[0]+" "+splits[1]
                    datetime_list.append(datetime.datetime.strptime(time_splits, "%Y-%m-%d %H:%M:%S"))
        return "Never" if len(datetime_list) == 0 else max(datetime_list)

def get_last_checked_updates():
    from datetime import datetime as dt

    from lib.manage_distro import get_check_update_log_file as get_cfile

    timestamp = get_file_timestamp(get_cfile())
    return "Never" if timestamp == "Never" else dt.fromtimestamp(timestamp)

def get_peripheral_hw_info():
    try:
        proc = Popen(['lspci -vv | grep -i "system peripheral"'], 
        stdout=PIPE,stderr=STDOUT,shell=True)
        out = proc.stdout.read().decode("UTF-8")
        print(out)
        return fixstring(out,prefix='System peripheral:') if out else "Not available"
    except:
        return "Not available"

print(get_peripheral_hw_info())
