from pathlib import Path
import time
import paramiko


DEVICE = {
    "host": "192.168.56.101",
    "port": 22,
    "username": "cisco",
    "password": "cisco123!"
}

OUTPUT_DIR = Path(__file__).resolve().parent / "andy_outputs"


def read_output(shell, wait_time=1):
    time.sleep(wait_time)
    output = ""

    while shell.recv_ready():
        output += shell.recv(65535).decode("utf-8", errors="ignore")
        time.sleep(0.2)

    return output


def run_device_commands(config_commands, verify_commands, output_filename):
    OUTPUT_DIR.mkdir(exist_ok=True)
    full_output = ""

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Connecting to CSR1000v device...")

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
        full_output += read_output(shell)

        shell.send("enable\n")
        full_output += read_output(shell)

        if "Password" in full_output:
            shell.send(DEVICE["password"] + "\n")
            full_output += read_output(shell)

        shell.send("terminal length 0\n")
        full_output += read_output(shell)

        shell.send("configure terminal\n")
        full_output += read_output(shell)

        for command in config_commands:
            shell.send(command + "\n")
            full_output += read_output(shell)

        shell.send("end\n")
        full_output += read_output(shell)

        shell.send("write memory\n")
        full_output += read_output(shell, 2)

        for command in verify_commands:
            shell.send(command + "\n")
            full_output += read_output(shell, 2)

        ssh.close()

        output_path = OUTPUT_DIR / output_filename
        output_path.write_text(full_output)

        print(full_output)
        print(f"\nOutput saved to: {output_path}")

    except Exception as error:
        print("Configuration failed.")
        print("Error:", error)
