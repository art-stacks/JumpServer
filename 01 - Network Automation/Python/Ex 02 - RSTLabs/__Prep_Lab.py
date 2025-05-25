from netmiko import ConnectHandler


## Get Device Information
vm_ip = input('What is the ipv4 address of your RSTHayup VM? (x.x.x.x): ')
user_name = 'admin'
user_pass = 'pass'
enable_secret = 'pass'


# Values for ConnectHandler
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': vm_ip,
    'username': user_name,
    'password': user_pass,
    'secret': enable_secret,
    'port': 2001
}


# Device Port Numbers
p1 = 2001
p2 = 2002
a1 = 2003
a2 = 2004
s1 = 2005
d1 = 2006
d2 = 2007
s2 = 2008

## Device Configurations
p1_config = [
    'int e0/0',
    'ip add 172.16.255.101 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]

p2_config = [
    'int e1/0',
    'ip add 172.16.255.102 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]

s1_config = [
    'int e1/0',
    'ip add 172.16.255.111 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]

s2_config = [
    'int e1/0',
    'ip add 172.16.255.112 255.255.255.128',
    'no shut',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]

a1_config = [
    'vlan 12',
    'name realworld',
    'int vlan 12',
    'ip add 172.16.255.1 255.255.255.128',
    'no shut',
    'exit',
    'int e0/0',
    'sw mo ac',
    'sw ac vlan 12',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]

a2_config = [
    'vlan 12',
    'name realworld',
    'int vlan 12',
    'ip add 172.16.255.2 255.255.255.128',
    'no shut',
    'exit',
    'int e1/0',
    'sw mo ac',
    'sw ac vlan 12',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]

d1_config = [
    'ip routing'
    'vlan 12',
    'name realworld',
    'int vlan 12',
    'ip add 172.16.255.3 255.255.255.128',
    'no shut',
    'exit',
    'int e1/0',
    'sw mo ac',
    'sw ac vlan 12',
    'int e3/3',
    'no shut',
    'no sw',
    'ip add dhcp',
    'end'
]

d2_config = [
    'vlan 12',
    'name realworld',
    'int vlan 12',
    'ip add 172.16.255.4 255.255.255.128',
    'no shut',
    'exit',
    'int e1/0',
    'sw mo ac',
    'sw ac vlan 12',
    'ip route 0.0.0.0 0.0.0.0 172.16.255.3',
    'end'
]


## CONNECT To Devices
# Device to connect
device_list = ['P1', 'P2', 'S1', 'S2', 'A1', 'A2', 'D1', 'D2']

for device in device_list:
    # Specify port number of the device
    if device == 'P1': 
        device_info['port'] = p1
    elif device == 'P2':
        device_info['port'] = p2
    elif device == 'S1':
        device_info['port'] = s1
    elif device == 'S2':
        device_info['port'] = s2
    elif device == 'A1':
        device_info['port'] = a1
    elif device == 'A2':
        device_info['port'] = a2
    elif device == 'D1':
        device_info['port'] = d1
    elif device == 'D2':
        device_info['port'] = d2
    print(f"Configuring {device} ")
    # PUSH Configurations
    accesscli = ConnectHandler(**device_info)
    accesscli.enable()

        # Specify port number of the device
    if device == 'P1': 
        accesscli.send_config_set(p1_config)
    elif device == 'P2':
        accesscli.send_config_set(p2_config)
    elif device == 'S1':
        accesscli.send_config_set(s1_config)
    elif device == 'S2':
        accesscli.send_config_set(s2_config)
    elif device == 'A1':
        accesscli.send_config_set(a1_config)
    elif device == 'A2':
        accesscli.send_config_set(a2_config)
    elif device == 'D1':
        accesscli.send_config_set(d1_config)
    elif device == 'D2':
        accesscli.send_config_set(d2_config)
        
    print(f"Configuration Complete!")
    
print(f'RST ({vm_ip}) Configured Successfully!!')
