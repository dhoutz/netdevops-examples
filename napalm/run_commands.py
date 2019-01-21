from napalm import get_network_driver
from pprint import pprint

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'

driver = get_network_driver('junos')
device = driver(hostname=host, username=user, password=passwd)

device.open()

if device.is_alive():
   command_list = ['show version', 'show chassis hardware', 'show system uptime']
   output = device.cli(command_list)
   pprint(output)
else:
    pprint('Device is unreachable!')