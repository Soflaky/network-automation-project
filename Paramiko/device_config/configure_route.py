from kwan_ssh_helper import run_device_commands


def main():
    config_commands = [
        "ip route 203.0.113.0 255.255.255.0 Null0"
    ]

    verify_commands = [
        "show running-config | include ip route 203.0.113.0",
        "show ip route static"
    ]

    run_device_commands(
        config_commands=config_commands,
        verify_commands=verify_commands,
        output_filename="static_route_output.txt"
    )


if __name__ == "__main__":
    main()
