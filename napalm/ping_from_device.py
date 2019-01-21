from napalm import get_network_driver
from pprint import pprint

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'
host_to_ping = '8.8.8.8'
ping_count = 10
ping_size = 64

driver = get_network_driver('junos')
device = driver(hostname=host, username=user, password=passwd)

device.open()

ping_results = device.ping(destination=host_to_ping, size=ping_size, count=ping_count)

pprint(ping_results)



''' ping parameters supported '''

'''
:param destination: Host or IP Address of the destination
:param source (optional): Source address of echo request
:param ttl (optional): Maximum number of hops
:param timeout (optional): Maximum seconds to wait after sending final packet
:param size (optional): Size of request (bytes)
:param count (optional): Number of ping request to send

'''