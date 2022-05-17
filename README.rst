一个获取远程linux服务器信息的工具
---------------------------------

example
=======

code:: python

   from Azog.base.exception import HostClientException
   from Azog import Host

   hosts = [
       {'Address': '192.223.42.25', 'Port': 22, 'User': 'root', 'Password': '123456'},

   ]

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

               # sftp
               h.sftp_get('/root/111/2131', '1')
               h.sftp_put('demo.py', '/root/111/demo.py')

               print('*' * 50)
           except HostClientException as e:
               print(e.code, e.message)
           except Exception as e:
               print(e)