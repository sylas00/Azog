from base.base_host import BaseHost
from base.exception import HostClientException
from base.command import command_dict
from server_info.cpu_info import CpuInfo
from server_info.disk_info import DiskInfo
from server_info.ram_info import RamInfo
from server_info.system_info import SystemInfo

hosts = [
    {'Address': '192.222.5.2', 'Port': 22, 'User': 'root', 'Password': 'donotuseroot!'},
    {'Address': '194.156.224.51', 'Port': 22, 'User': 'root', 'Password': 'Maijia123..'},
]


class Host(BaseHost):
    def __init__(self, host_connect_info: dict):
        super().__init__(host_connect_info)
        self.cpu_info = CpuInfo(client=self.client)
        self.disk_info = DiskInfo(client=self.client)
        self.ram_info = RamInfo(client=self.client)
        self.sys_info = SystemInfo(client=self.client)
        self.execute(command_dict.get('close_history'))

    def __del__(self):
        if hasattr(self, 'client'):
            self.execute(command_dict.get('open_history'))
            self.client.close()


if __name__ == '__main__':

    for i in hosts:
        try:
            h = Host(i)
            # system
            print(h.sys_info.get_uptime())
            print(h.sys_info.get_load())
            print(h.sys_info.get_kernel())
            print(h.sys_info.get_release())
            print(h.sys_info.get_architecture())
            # cpu
            print(h.cpu_info.get_cpu_name())
            print(h.cpu_info.get_cpu_cores())
            print(h.cpu_info.get_cpu_freq())
            print(h.cpu_info.get_cpu_core_cache())
            # ram
            print(h.ram_info.get_total_ram())
            print(h.ram_info.get_use_ram())
            print(h.ram_info.get_buff_ram())
            print(h.ram_info.get_total_swap())
            print(h.ram_info.get_use_swap())
            # disk
            print(h.disk_info.get_total_disk())
            print(h.disk_info.get_use_disk())

            print('*' * 50)
        except HostClientException as e:
            print(e.code, e.message)
        except Exception as e:
            print(e)
