from kwan_ssh_helper import run_device_commands


def main():
    config_commands = [
        "username kwan privilege 15 secret Kwan12345"
    ]

    verify_commands = [
        "show running-config | include username kwan"
    ]

    run_device-commands(
        conffig_commands=config_commands,
        verify_commands=verify_commands,
        output_filename="user_config_output.txt"
    )

if __name__ == "__main__":
    main()
