from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': 'Host_IP',
    'username': 'Your_user_Name',
    'password': 'Your_Password',
   
    
}
ssh= ConnectHandler(**device)
ssh.enable()
output = ssh.send_command('show ip interface brief')
print(output)
