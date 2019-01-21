from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'
remote_path='/var/tmp'
file='hello_world.txt'

dev = Device(host=host, user=user, password=passwd)

#Upload file
with SCP(dev, progress=True) as scp:
    scp.put(file, remote_path)
