# Member 4 Testing Notes

Member Name:
Mohamed

Task:
Retrieve network device information from CSR1000v.

Tools Used:
Python
Paramiko
SSH
Git
GitHub

Files Created:
device_info/retrieve_info.py
device_info/mohammed_outputs/device_report.txt

Device Access Information:
Device IP: 192.168.56.101
Username: cisco
Password: cisco123!

Information Retrieved:
1. Hostname
2. Device version
3. Interface information
4. Routing table
5. Running configuration

Command Used:
python3 device_info/retrieve_info.py

Verification Commands Used by Script:
show running-config | include hostname
show version
show ip interface brief
show ip route
show running-config

Result:
Mohammed successfully retrieved device information and saved the output into device_report.txt.
