from jnpr.junos import Device
from pprint import pprint

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'

with Device(host=host, user=user, password=passwd) as dev:
    pprint (dev.facts)
