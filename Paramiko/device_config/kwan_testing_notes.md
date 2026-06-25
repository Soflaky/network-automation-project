# Member 3 Testing Notes

Member Name:
Kwan

Task:
Configure user account, banner message, and static route on CSR1000v.

Tools Used:
Python
Paramiko
SSH
Git
GitHub

Files Created:
device_config/kwan_ssh_helper.py
device_config/configure_user.py
device_config/configure_banner.py
device_config/configure_route.py

Configuration Applied:

1. User Account
Username: kwan
Privilege: 15
Password: Kwan12345

2. Banner Message
UNAUTHORIZED ACCESS PROHIBITED - CONFIGURED BY KWAN

3. Static Route
Destination Network: 203.0.113.0
Subnet Mask: 255.255.255.0
Exit Interface: Null0

Commands Used:
python3 device_config/configure_user.py
python3 device_config/configure_banner.py
python3 device_config/configure_route.py

Verification Commands:
show running-config | include username andy
show running-config | include banner
show running-config | include ip route 203.0.113.0
show ip route static

Result:
The user account, banner message, and static route were configured successfully.
