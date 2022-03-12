from linux_manager.base.base_host import BaseHost
from linux_manager.base.command import command_dict
from linux_manager.server_info.info_utils import handler_uptime_info


class SystemInfo(BaseHost):
    def get_release(self):
        result = self.execute(command_dict.get('release'))
        return result.split('\n')[0]

    def get_uptime(self):
        return self.execute(command_dict.get('uptime'))

    def get_load(self):
        return self.execute(command_dict.get('load'))

    def get_architecture(self):
        return self.execute(command_dict.get('architecture'))

    def get_kernel(self):
        return self.execute(command_dict.get('kernel'))

    def get_uptime_info(self) -> float:
        """弃用 暂时先留着"""
        return handler_uptime_info(self.execute('cat /proc/uptime'))