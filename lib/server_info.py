import lib
from cpuinfo import get_cpu_info
from psutil import virtual_memory, disk_usage


def get_processor():
    return get_cpu_info()['brand_raw']


def get_installed_memory():
    return str(round((virtual_memory().total)/(1024**3))) + ' GB'


def get_total_disk_space():
    return str(round((disk_usage('/').total)/(1024**3))) + ' GB'
