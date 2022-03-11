import paramiko

from exception import InitHostException, HostClientException, ExecuteCommandException
from utils import handler_memory_info, handler_system_info, handler_disk_info, handler_uptime_info

hosts = [
    # {'Address': '192.222.5.2', 'Port': 22, 'User': 'root', 'Password': 'donotuseroot!'},
    {'Address': '194.156.224.51', 'Port': 22, 'User': 'root', 'Password': 'Maijia123..'},
]


class Host:
    def __init__(self, host_connect_info: dict):
        self.connect_address = host_connect_info.get('Address', None)
        self.connect_port = host_connect_info.get('Port', None)
        self.connect_name = host_connect_info.get('User', None)
        self.connect_password = host_connect_info.get('Password', None)
        if not all([self.connect_port, self.connect_address, self.connect_name, self.connect_password]):
            raise InitHostException()
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.connect_address, self.connect_port, self.connect_name, self.connect_password)

    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()

    def get_system_info(self) -> dict:
        return handler_system_info(self.execute('hostnamectl'))

    def get_memory_info(self) -> dict:
        return handler_memory_info(self.execute('free'))

    def get_disk_info(self) -> dict:
        total = self.execute(
            "LANG=C df -hPl | grep -wvE '\-|none|tmpfs|overlay|shm|udev|devtmpfs|by-uuid|chroot|Filesystem' | awk '{print $2}' ")
        use = self.execute(
            "LANG=C df -hPl | grep -wvE '\-|none|tmpfs|overlay|shm|udev|devtmpfs|by-uuid|chroot|Filesystem' | awk '{print $3}'")
        return handler_disk_info(total, use)

    def get_uptime_info(self) -> float:
        return handler_uptime_info(self.execute('cat /proc/uptime'))

    def execute(self, command: str) -> str:
        stdin, stdout, stderr = self.client.exec_command(command)
        rsp = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        if error:
            raise ExecuteCommandException(error)
        return rsp


if __name__ == '__main__':

    for i in hosts:
        try:
            h = Host(i)

            # print(h.get_system_info())
            # print(h.get_memory_info())
            # print(h.get_disk_info())
            print(h.get_uptime_info())

            print('*' * 50)
        except HostClientException as e:
            print(e.code, e.message)
        except Exception as e:
            print(e)
