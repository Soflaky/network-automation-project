# Member 2 Testing Notes

## Task

Amr configured a network device interface using Ansible.

## Tools Used

- Ansible
- Cisco IOS modules
- Git
- GitHub

## Files Created

- ansible/amr_interface_config/hosts
- ansible/amr_interface_config/ansible.cfg
- ansible/amr_interface_config/configure_ip.yaml
- ansible/amr_interface_config/configure_description.yaml
- device_config/configure_ip.py
- device_config/configure_interface.py

## Configuration Applied

Interface:
Loopback10

IP address:
202.6.255.1

Subnet mask:
255.255.255.252

Description:
configured by amr using ansible

## Commands Used

ansible-playbook configure_ip.yaml
ansible-playbook configure_description.yaml
python3 device_config/configure_ip.py
python3 device_config/configure_interface.py

## Verification Commands

show ip interface brief
show running-config interface Loopback10

## Result

The IP address and interface description were configured successfully and verified through Cisco IOS CLI.
