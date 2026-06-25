from andy_ssh_helper import run_device_commands


def main():
    config_commands = [
        "username kwon privilege 15 password Kwon12345"
    ]

    verify_commands = [
        "show running-config | include username kwon"
    ]

    run_device_commands(
        config_commands=config_commands,
        verify_commands=verify_commands,
        output_filename="user_config_output.txt"
    )


if __name__ == "__main__":
    main()
