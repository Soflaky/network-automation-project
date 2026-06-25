from pathlib import Path
from datetime import datetime
import socket
import platform
import psutil
import shutil
import time


OUTPUT_DIR = Path(__file__).resolve().parent / "ammar_outputs"
OUTPUT_FILE = OUTPUT_DIR / "linux_system_report.txt"


def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)


def get_cpu_name():
    cpu_name = platform.processor()

    if cpu_name:
        return cpu_name

    try:
        with open("/proc/cpuinfo", "r") as file:
            for line in file:
                if "model name" in line:
                    return line.split(":", 1)[1].strip()
    except FileNotFoundError:
        pass

    return "CPU information not available"


def get_logged_in_users():
    users = psutil.users()

    if not users:
        return ["No logged-in users detected"]

    return sorted(set(user.name for user in users))


def get_top_processes():
    processes = []

    for process in psutil.process_iter(["pid", "name"]):
        try:
            process.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    time.sleep(1)

    for process in psutil.process_iter(["pid", "name", "cpu_percent"]):
        try:
            info = process.info
            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "cpu": process.cpu_percent(interval=None)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(processes, key=lambda item: item["cpu"], reverse=True)

    return processes[:5]


def generate_report():
    OUTPUT_DIR.mkdir(exist_ok=True)

    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu_name = get_cpu_name()
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    disk = shutil.disk_usage("/")

    users = get_logged_in_users()
    top_processes = get_top_processes()

    report = []

    report.append("Linux System Information Report")
    report.append("===============================")
    report.append("Collected By: Ammar")
    report.append(f"Date and Time: {current_time}")
    report.append("")

    report.append("Hostname")
    report.append("--------")
    report.append(hostname)
    report.append("")

    report.append("CPU Information")
    report.append("---------------")
    report.append(f"CPU Name: {cpu_name}")
    report.append(f"CPU Cores: {cpu_cores}")
    report.append(f"CPU Usage: {cpu_usage}%")
    report.append("")

    report.append("Memory Usage")
    report.append("------------")
    report.append(f"Total Memory: {bytes_to_gb(memory.total)} GB")
    report.append(f"Used Memory: {bytes_to_gb(memory.used)} GB")
    report.append(f"Available Memory: {bytes_to_gb(memory.available)} GB")
    report.append(f"Memory Usage: {memory.percent}%")
    report.append("")

    report.append("Disk Usage")
    report.append("----------")
    report.append(f"Total Disk: {bytes_to_gb(disk.total)} GB")
    report.append(f"Used Disk: {bytes_to_gb(disk.used)} GB")
    report.append(f"Free Disk: {bytes_to_gb(disk.free)} GB")
    report.append("")

    report.append("Logged-in Users")
    report.append("---------------")
    for user in users:
        report.append(user)
    report.append("")

    report.append("Top 5 Processes by CPU Usage")
    report.append("----------------------------")

    if not top_processes:
        report.append("No process information available")
    else:
        for index, process in enumerate(top_processes, start=1):
            report.append(
                f"{index}. PID: {process['pid']} | "
                f"Name: {process['name']} | "
                f"CPU: {process['cpu']}%"
            )

    final_report = "\n".join(report)

    OUTPUT_FILE.write_text(final_report)

    print(final_report)
    print("")
    print(f"Report saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_report()
