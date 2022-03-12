from base.base_host import BaseHost
from base.command import command_dict
from server_info.info_utils import handler_memory_info


class RamInfo(BaseHost):

    def get_total_ram(self):
        return self.execute(command_dict.get('total_ram'))

    def get_use_ram(self):
        return self.execute(command_dict.get('use_ram'))

    def get_buff_ram(self):
        return self.execute(command_dict.get('buff_ram'))

    def get_total_swap(self):
        return self.execute(command_dict.get('use_swap'))

    def get_use_swap(self):
        return self.execute(command_dict.get('total_ram'))

    def get_memory_info(self) -> dict:
        """弃用 暂时先留着"""
        return handler_memory_info(self.execute('free'))
