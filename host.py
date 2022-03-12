from base.base_host import BaseHost
from base.exception import HostClientException
from base.command import command_dict
from server_info.cpu_info import CpuInfo
from server_info.disk_info import DiskInfo
from server_info.ram_info import RamInfo
from server_info.system_info import SystemInfo

hosts = [
    # {'Address': '192.222.5.2', 'Port': 22, 'User': 'root', 'Password': 'donotuseroot!'},
    {'Address': '194.156.224.51', 'Port': 22, 'User': 'root', 'Password': 'Maijia123..'},
]


class Host(BaseHost):
    def __init__(self, host_connect_info: dict):
        super().__init__(host_connect_info)
        self.cpu_info = CpuInfo(client=self.client)
        self.disk_info = DiskInfo(client=self.client)
        self.ram_info = RamInfo(client=self.client)
        self.sys_info = SystemInfo(client=self.client)

    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()


if __name__ == '__main__':

    for i in hosts:
        try:
            h = Host(i)
            # ram
            print(h.ram_info.get_memory_info())
            # cpu
            print(h.cpu_info.get_cpu_name())
            print(h.cpu_info.get_cpu_cores())
            print(h.cpu_info.get_cpu_cores())
            print(h.cpu_info.get_cpu_core_cache())
            # disk
            print(h.ram_info.get_memory_info())
            print(h.ram_info.get_memory_info())
            # stata
            print('*' * 50)
        except HostClientException as e:
            print(e.code, e.message)
        except Exception as e:
            print(e)
