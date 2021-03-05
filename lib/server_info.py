import psutil
from cpuinfo import get_cpu_info
from psutil import disk_usage, virtual_memory


def get_processor():
    return get_cpu_info()['brand_raw']

def get_cpu_usage():
        cpu = psutil.cpu_percent(interval=1)
        return str(cpu) + "%"

def get_total_ram():
    return round(psutil.virtual_memory().total/(1024**3))
def get_used_ram():
    return round(psutil.virtual_memory().used/(1024**3))
def get_free_ram():
    return round(psutil.virtual_memory().free/(1024**3))



def disks_list():
    li =[]
    for disk in psutil.disk_partitions():
        li.append(disk[1])
    return li

def disk_total_space(disk_mountpoint):
    return round(psutil.disk_usage(disk_mountpoint).total/(1024**3))

def disk_used_space(disk_mountpoint):
    return round(psutil.disk_usage(disk_mountpoint).used/(1024**3))

def disk_free_space(disk_mountpoint):
    return round(psutil.disk_usage(disk_mountpoint).free/(1024**3))
