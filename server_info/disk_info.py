from base.base_host import BaseHost
from base.command import command_dict
from server_info.info_utils import handler_disk_info


class DiskInfo(BaseHost):
    def get_disk_info(self) -> dict:
        """弃用 暂时先留着"""
        total = self.execute(
            command_dict.get('total_disk'))
        use = self.execute('use_disk')
        return handler_disk_info(total, use)
