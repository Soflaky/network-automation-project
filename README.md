# Network Device Automation and Linux System Monitoring
## Project Description
This project automates network device configuration and Linux system information collection using
Python, NETCONF, Docker, and GitHub.
## Main Functions
### Network Device Automation
The system can automate the following configurations:
1. IP address configuration
2. User account configuration
3. Banner message configuration
4. Interface description configuration
5. Static route configuration
6. Network device information retrieval
### Linux System Monitoring
The system can collect:
1. Hostname
2. Current date and time
3. CPU information
4. Memory usage
5. Disk usage
6. Logged-in users
7. Top 5 running processes by CPU usage
## Tools Used
- Python
- NETCONF
- ncclient
- Docker
- Git
- GitHub
## Project Structure
```text
network-automation-project/
│
├── common/
│ └── netconf_connection.py
│
├── device_config/
│
├── device_info/
│├── linux_monitor/
│
├── docker/
│
├── screenshots/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
