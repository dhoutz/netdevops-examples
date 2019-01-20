from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP

host = '192.168.2.117'
user = 'root'
passwd = 'Juniper'
remote_path='/var/tmp'
file='/Users/dhoutz/Downloads/vmx-bundle-17.4R2.4.tgz'

dev = Device(host=host, user=user, password=passwd)

#Upload file
with SCP(dev, progress=True) as scp:
    scp.put(file, remote_path)
