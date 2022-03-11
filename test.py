import paramiko

hosts = [
    {'Address': '192.222.5.2', 'Port': 22, 'User': 'root', 'Password': 'donotuseroot!'},
    {'Address': '194.156.224.51', 'Port': 22, 'User': 'root', 'Password': 'Maijia123..'},
]


class InitHostException(Exception):
    def __init__(self, message, ):
        super().__init__()
        self.message = message


class Host:
    def __init__(self, host_connect_info: dict):
        self.connect_address = host_connect_info.get('Address', None)
        self.connect_port = host_connect_info.get('Port', None)
        self.connect_name = host_connect_info.get('User', None)
        self.connect_password = host_connect_info.get('Password', None)
        if not all([self.connect_port, self.connect_address, self.connect_name, self.connect_password]):
            raise InitHostException('你他吗少填信息了')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.connect_address, self.connect_port, self.connect_name, self.connect_password)

    def __del__(self):
        self.client.close()

    @staticmethod
    def handler_system_info(info_stdout: str) -> dict:
        info_list = info_stdout.splitlines()
        machine_info_dict = {}
        for _ in info_list:
            line_info = _.strip()
            info_name, *junk, info_value = [_i.strip() for _i in line_info.partition(':')]
            machine_info_dict[info_name] = info_value
        return machine_info_dict

    def get_system_info(self) -> dict:
        stdin, stdout, stderr = self.client.exec_command('hostnamectl')
        rsp = stdout.read().decode('utf-8')
        return self.handler_system_info(rsp)

    @staticmethod
    def handler_memory_info(info_stdout: str) -> dict:
        info_list = info_stdout.splitlines()[1:]
        memory_info_dict = {}
        for _ in info_list:
            a = _.split()[:3]
            memory_info_dict[a[0]] = {'total': int(a[1]), 'use': int(a[2])}
        return memory_info_dict

    def get_memory_info(self) -> dict:
        stdin, stdout, stderr = self.client.exec_command('free')
        rsp = stdout.read().decode('utf-8')
        return self.handler_memory_info(rsp)


if __name__ == '__main__':

    for i in hosts:
        h = Host(i)
        print(h.get_system_info())
        print(h.get_memory_info())
        print('*' * 50)
