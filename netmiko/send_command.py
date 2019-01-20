from netmiko import ConnectHandler

dev = {
    'device_type': 'juniper',
    'ip':   '192.168.2.117',
    'username': 'juniper',          # NOTE: using 'root' for Juniper fails as you aren't put into cli
    'password': 'Juniper',
}

net_connect = ConnectHandler(**dev)

output = net_connect.send_command('show version and haiku')
print(output)