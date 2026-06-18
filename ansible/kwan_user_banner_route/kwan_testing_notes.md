# Testing Notes

## Task
Configure user account, banner message, and static route using Ansible.

## Files Created
- configure_user.yaml
- configure_banner.yaml
- configure_route.yaml
- configure_user.py
- configure_banner.py
- configure_route.py

## Verification Commands

show running-config | include username

show running-config | section banner

show ip route static

## Result

All configurations were successfully deployed and verified.

