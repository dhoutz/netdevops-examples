from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'

with Device(host=host, user=user, password=passwd) as dev:
    dev.open()
    sw = SW(dev)
    print(sw.inventory)
