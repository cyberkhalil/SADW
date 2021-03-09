from psutil import cpu_percent, disk_partitions, disk_usage, virtual_memory


def get_osversion():
    try:
        import platform
        return platform.platform()
    except:
        return "module platform not found"


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
