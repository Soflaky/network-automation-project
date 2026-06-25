from pathlib import Path
from datetime import datetime
import time
import paramiko


DEVICE = {
    "host": "192.168.56.101",
    "port": 22,
    "username": "cisco",
    "password": "cisco123!"
}

OUTPUT_DIR = Path(__file__).resolve().parent / "mohamed_outputs"
REPORT_FILE = OUTPUT_DIR / "device_report.txt"


COMMANDS = {
    "Hostname": "show running-config | include hostname",
    "Device Version": "show version",
    "Interface Information": "show ip interface brief",
    "Routing Table": "show ip route",
    "Running Configuration": "show running-config"
}


def read_output(shell, wait_time=1.5):
    time.sleep(wait_time)
    output = ""

    while shell.recv_ready():
        output += shell.recv(65535).decode("utf-8", errors="ignore")
        time.sleep(0.2)

    return output


def send_command(shell, command, wait_time=2):
    shell.send(command + "\n")
    return read_output(shell, wait_time)


def collect_device_information():
    OUTPUT_DIR.mkdir(exist_ok=True)

    report_sections = []

    try:
        print("Connecting to CSR1000v device...")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=DEVICE["host"],
            port=DEVICE["port"],
            username=DEVICE["username"],
            password=DEVICE["password"],
            look_for_keys=False,
            allow_agent=False,
            timeout=10
        )

        shell = ssh.invoke_shell()
        read_output(shell)

        send_command(shell, "terminal length 0")

        report_sections.append("Device Information Report")
        report_sections.append("=========================")
        report_sections.append(f"Collected By: Mohamed")
        report_sections.append(f"Date and Time: {datetime.now()}")
        report_sections.append(f"Device IP: {DEVICE['host']}")
        report_sections.append("")

        for section_name, command in COMMANDS.items():
            print(f"Retrieving {section_name}...")

            output = send_command(shell, command, wait_time=3)

            report_sections.append("\n" + "=" * 60)
            report_sections.append(section_name)
            report_sections.append("=" * 60)
            report_sections.append(f"Command Used: {command}")
            report_sections.append("")
            report_sections.append(output)

        ssh.close()

        final_report = "\n".join(report_sections)
        REPORT_FILE.write_text(final_report)

        print("\nDevice information retrieved successfully.")
        print(f"Report saved to: {REPORT_FILE}")

    except Exception as error:
        print("Failed to retrieve device information.")
        print("Error:", error)


if __name__ == "__main__":
    collect_device_information()
