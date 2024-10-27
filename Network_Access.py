from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.137.6',
    'username': 'jeba',
    'password': 'jeba1234',
   
    
}
ssh= ConnectHandler(**device)
ssh.enable()
output = ssh.send_command('show ip interface brief')
print(output)