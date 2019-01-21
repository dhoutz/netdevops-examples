from jnpr.junos import Device
from lxml import etree
from pprint import pprint

host = '192.168.2.2'
user = 'juniper'
passwd = 'Juniper'


''' Get full config in XML'''
with Device(host=host, user=user, password=passwd) as dev:
    ''' Get full config in XML'''
    data = dev.rpc.get_config()
    print(etree.tostring(data, encoding='unicode'))

    print('=' * 80)

    ''' Get a specific section of config'''
    data = dev.rpc.get_config(filter_xml='<system><services/></system>')
    print(etree.tostring(data, encoding='unicode'))

    print('=' * 80)

    ''' Or with a cleaner XML path syntax'''
    data = dev.rpc.get_config(filter_xml='system/services')
    print(etree.tostring(data, encoding='unicode'))

    print('=' * 80)

    ''' Get config in JSON format'''
    data = dev.rpc.get_config(options={'format': 'json'})
    pprint(data)

    print('=' * 80)

    ''' Get section of config in JSON format'''
    data = dev.rpc.get_config(filter_xml='system/services', options={'format': 'json'})
    pprint(data)

    print('=' * 80)

    ''' Get Junos and YANG model configs'''
    data = dev.rpc.get_config(model=True)
    print(etree.tostring(data, encoding='unicode'))
