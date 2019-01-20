from jnpr.junos import Device
from pprint import pprint

host = '192.168.2.117'
user = 'root'
passwd = 'Juniper'

with Device(host=host, user=user, password=passwd) as dev:
    pprint (dev.facts)
