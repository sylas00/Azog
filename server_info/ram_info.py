from base.base_host import BaseHost
from server_info.info_utils import handler_memory_info


class RamInfo(BaseHost):

    def get_memory_info(self) -> dict:
        return handler_memory_info(self.execute('free'))
