import psutil
from os import name

class Server:
    def __init__(self):
        self.name = name
        self.cpuCores = psutil.cpu_count(logical=False)

        self.memory = psutil.virtual_memory()
        self.swap = psutil.swap_memory()
        self.disk = psutil.disk_usage('/')
        self.diskIO = psutil.disk_io_counters()
        self.net = psutil.net_io_counters()

    def update_psutils(self):
        self.memory = psutil.virtual_memory()
        self.swap = psutil.swap_memory()
        self.disk = psutil.disk_usage('/')
        self.diskIO = psutil.disk_io_counters()
        self.net = psutil.net_io_counters()

    def cpu_usage(self):
        return psutil.cpu_percent(percpu=False, interval=0.15)

