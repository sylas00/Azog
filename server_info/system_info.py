from base.base_host import BaseHost
from server_info.info_utils import handler_uptime_info


class SystemInfo(BaseHost):

    def get_uptime_info(self) -> float:
        return handler_uptime_info(self.execute('cat /proc/uptime'))
