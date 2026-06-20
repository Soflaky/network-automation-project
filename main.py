from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent

SCRIPTS = {
    "1": ("Configure IP address", "device_config/configure_ip.py"),
    "2": ("Configure interface description", "device_config/configure_interface.py"),
    "3": ("Configure user account", "device_config/configure_user.py"),
    "4": ("Configure banner message", "device_config/configure_banner.py"),
    "5": ("Configure static route", "device_config/configure_route.py"),
    "6": ("Retrieve device information", "device_info/retrieve_info.py"),
    "7": ("Show Linux system information", "linux_monitor/linux_monitor.py"),
}

def run_script(script_path):
    full_path = BASE_DIR / script_path
    if not full_path.exists():
        print(f"\nThis script is not implemented yet: {script_path}")
        print("The responsible member still needs to add this file.\n")
        return
    subprocess.run([sys.executable, str(full_path)], check=False)

def show_menu():
    print("\nNetwork Automation Project")
    print("--------------------------")
    for key, value in SCRIPTS.items():
        print(f"{key}. {value[0]}")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        if choice == "0":
            print("Exiting program.")
            break
        if choice in SCRIPTS:
            run_script(SCRIPTS[choice][1])
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
