#! /usr/bin/env python3

import os
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)


def cls(): return os.system('clear')

"""
    sendTree: Sends a system command to the target host computer system, then outputs the results to standard out.
          @params ip:       The hostname or IP address of the target system
    @params username:       A username from the system's accounts
    @params password:       The user's password
        @params port:       The port to make the connection
"""


def sendTreePass(ip, username, password, port):
    try:
        device = ConnectHandler(
            device_type='autodetect', ip=ip, username=username, port=port, password=password)

        output = device.send_command("tree")

        cls()

        print("\n\n\tMethod: sendTree\n\tHost: {0}\n\tUser: {1}\n\tCommand: {2}\n\tPort: {3}\n\n".format(
            ip, username, "tree", port))

        print(output)

        device.disconnect()

    except NetmikoTimeoutException:
        print("\n\n\tTimeout Error: System may not be online")

    except NetmikoAuthenticationException:
        print("\n\n\tAuthentication Error: Bad username, password or publicKey")

    except:
        print("\n\n\t{0}\n\n".format("Something else went horribly wrong"))


"""
    sendTree: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params key_file_path:      The absolute path to the private key file to access the host
    @params pass_phrase         The passphrase for the private key
    @params port:               The port to make the connection
"""


def sendTreeKey(ip, username, key_file_path, pass_phrase, port):
    try:
        device = ConnectHandler(
            device_type='autodetect', ip=ip, username=username, port=port, use_keys=True, passphrase=pass_phrase, key_file=key_file_path)

        output = device.send_command("tree")

        print("\n\n\tMethod: sendTree\n\tHost: {0}\n\tUser: {1}\n\tCommand: {2}\n\tPort: {3}\n\n".format(
            ip, username, "tree", port))

        print(output)

        device.disconnect()

    except NetmikoTimeoutException:
        print("\n\n\tTimeout Error: {0}\n\n".format(
            NetmikoTimeoutException))

    except NetmikoAuthenticationException:
        print("\n\n\tAuthentication Error: {0}\n\n".format(
            NetmikoAuthenticationException.cause))

    except:
        print("\n\n\t{0}\n\n".format("Something else went horribly wrong"))
