from napalm import get_network_driver
from pprint import pprint

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'
destination = '8.8.8.8'

driver = get_network_driver('junos')
device = driver(hostname=host, username=user, password=passwd)

device.open()

trace_results = device.traceroute(destination=destination)

pprint(trace_results)

''' traceroute parameters supported '''

'''
:param destination: Host or IP Address of the destination
:param source (optional): Use a specific IP Address to execute the traceroute
:param ttl (optional): Maimum number of hops
:param timeout (optional): Number of seconds to wait for respons

'''