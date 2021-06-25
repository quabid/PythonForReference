#! /usr/bin/env python3

import os
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)
from getpass import getpass


def cls(): return os.system('clear')


def test():
    cls()
    try:
        device = ConnectHandler(
            device_type='autodetect', ip='192.168.1.20', username='sjhadmin', port="30777", password=getpass())
        output = device.send_command("tree")
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


test()
