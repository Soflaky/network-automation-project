from andy_ssh_helper import run_device_commands


def main():
    config_commands = [
        "banner motd #UNAUTHORIZED ACCESS PROHIBITED - CONFIGURED BY ANDY#"
    ]

    verify_commands = [
        "show running-config | include banner"
    ]

    run_device_commands(
        config_commands=config_commands,
        verify_commands=verify_commands,
        output_filename="banner_config_output.txt"
    )


if __name__ == "__main__":
    main()
