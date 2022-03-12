from base.base_host import BaseHost
from base.command import command_dict
from server_info.info_utils import handler_uptime_info


class SystemInfo(BaseHost):
    def get_uptime(self):
        return self.execute(command_dict.get('uptime'))

    def get_load(self):
        return self.execute(command_dict.get('load'))

    def get_uptime_info(self) -> float:
        """弃用 暂时先留着"""
        return handler_uptime_info(self.execute('cat /proc/uptime'))
