# Ammar's Testing Notes

Member Name:
Ammar

Task:
Collect Linux system information and run the monitoring script using Docker.

Tools Used:
Python
psutil
Docker
Docker Compose
Git
GitHub

Files Created:
linux_monitor/linux_monitor.py
linux_monitor/ammar_outputs/linux_system_report.txt
docker/Dockerfile
docker/docker-compose.yml

Information Collected:
1. Hostname
2. Current date and time
3. CPU information
4. Memory usage
5. Disk usage
6. Logged-in users
7. Top 5 running processes by CPU usage

Commands Used:
python3 linux_monitor/linux_monitor.py
docker compose -f docker/docker-compose.yml up --build

Result:
The Linux monitoring script successfully collected system information and saved it into linux_system_report.txt. The script was also tested inside Docker.
