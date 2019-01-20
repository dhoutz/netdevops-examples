from napalm import get_network_driver
from pprint import pprint

host = '192.168.2.117'
user = 'juniper'
passwd = 'Juniper'

driver = get_network_driver('junos')
device = driver(hostname=host, username=user, password=passwd)

device.open()

if device.is_alive():
    print('Connection successful!')
    pprint(device.get_facts())
else:
    print 'Device is unreachable!'