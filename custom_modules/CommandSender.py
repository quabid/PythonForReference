#! /usr/bin/env python3

import os
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)


def cls(): return os.system('clear')


"""
    sendCommand: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:             The hostname or IP address of the target system
    @params username:       A username from the system's accounts
    @params password:       The user's password
    @params command:        The command to send to the system
    @params port:           The port to connect with; defaults to 30777
"""


def sendCommand(ip, username, password, command, port):
    try:
        device = ConnectHandler(
            device_type='autodetect', ip=ip, username=username, port=port, password=password)

        output = device.send_command(command)

        cls()

        print("\n\n\tHost: {0}\n\tUser: {1}\n\tCommand: {2}\n\tPort: {3}\n\n".format(
            ip, username, command, port))

        print(output)

        device.disconnect()

    except NetmikoTimeoutException:
        print("\n\n\tTimeout Error: {0}\n\n".format(
            str(NetmikoTimeoutException)))

    except NetmikoAuthenticationException:
        print("\n\n\tAuthentication Error: {0}\n\n".format(
            str(NetmikoAuthenticationException)))

    except:
        print("\n\n\t{0}\n\n".format("Something else went horribly wrong"))
