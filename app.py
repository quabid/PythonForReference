#! /usr/bin/env python3
import sys
import os
from custom_modules.index import commandKey, commandPassword, treePass, treeKey, fileExists

ARG_COUNT = len(sys.argv)
ARGS = sys.argv
SWITCH = {
    "key": commandKey,
    "pass": commandPassword,
    "treePass": treePass,
    "treeKey": treeKey
}


def cls(): return os.system('clear')


def log(arg):
    print("{0}\n".format(str(arg)))


"""
commandPassword: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params password:           The user's password
    @params command:            The command to send to the system
    @params port:               The port to connect with; defaults to 30777

commandKey: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params key_file_path:      The absolute path to the private key file to access the host
    @params pass_phrase         The passphrase for the private key
    @params command:            The command to send to the system
    @params port:               The port to connect with; defaults to 30777

treePass: Sends the tree command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params password:           The user's password
    @params port:               The port to make the connection

treeKey: Sends the tree command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params key_file_path:      The absolute path to the private key file to access the host
    @params pass_phrase         The passphrase for the private key
    @params port:               The port to make the connection
"""


'''         CLI Usage

    sendCommandKey: app IP or Hostname Username Key_File_Path, Key_File_Passphrase Command Port

    sendCommandPassword: app IP or Hostname Username Password Command Port

    tree: app IP or Hostname Username Password Port
'''

print("\n\t\tArgument Count: {}\n".format(ARG_COUNT))

if ARG_COUNT == 7:
    # Send Command - Username and Password
    # app.py <[IP or Hostname]> <Username> <Password> <Command> <Port> <Keyword: "pass">
    key = ARGS[6].strip().lower()
    function = SWITCH[key]
    ip_or_hostname = ARGS[1]
    username = ARGS[2]
    password = ARGS[3]
    command = ARGS[4]
    port = ARGS[5]

    print("\n\tConnect with Password: {} {} {} {} {} {}\n\n".format(
        ip_or_hostname, username, password, command, port, key))

    function(ip_or_hostname, username, password, command, port)
elif ARG_COUNT == 8:
    # Send Command - Private Key
    # ./app.py <[IP or Hostname]> <username> </Path/To/Private/Key> <Private Key Passphrase> <Command> <Port> <Keyword:"key">
    cls()
    key = ARGS[7].strip().lower()
    function = SWITCH[key]
    ip_or_hostname = ARGS[1]
    username = ARGS[2]
    key_file_path = ARGS[3]
    key_file_passphrase = ARGS[4]
    command = ARGS[5]
    port = ARGS[6]
    log("\n\tStatement:\tapp.py {} {} {} {} {} {}\n\n".format(
        ip_or_hostname, username, key_file_path, key_file_passphrase, command, port))

    if fileExists(key_file_path):

        print("\n\tConnect with Key: {} {} {} {} {} {} {}\n\n".format(ip_or_hostname,
                                                                      username, key_file_path, key_file_passphrase, command, port, key))

        function(ip_or_hostname, username, key_file_path,
                 key_file_passphrase, command, port)

        log("\n")
    else:
        print("\n\tPrivate Key: {} does not exist\n\n".format(key_file_path))

elif ARG_COUNT == 5:
    # Send Tree Command: Username Password
    # app.py <[IP or Hostname]> <Username> <Password> <Port>
    key = "treePass"
    function = SWITCH[key]
    ip_or_hostname = ARGS[1]
    username = ARGS[2]
    password = ARGS[3]
    port = ARGS[4]

    print("\n\tConnect with Password:{} {} {} {} {} \n\n".format(ip_or_hostname,
          username, password, port, key))

    function(ip_or_hostname, username, password, port)
elif ARG_COUNT == 6:
    # Send Tree Command: Private Key
    # app.py <[IP or Hostname]> <Username> </Path/To/Private/Key> <Private Key Passphrase> <Port>
    key = "treeKey"
    function = SWITCH[key]
    ip_or_hostname = ARGS[1]
    username = ARGS[2]
    key_file_path = ARGS[3]
    key_file_passphrase = ARGS[4]
    port = ARGS[5]

    if fileExists(key_file_path):

        log("\n\tStatement:\tapp.py {} {} {} {} {}\n\n".format(
            ip_or_hostname, username, key_file_path, key_file_passphrase, port))

        print("\n\tConnect with Key:{} {} {} {} {} {} \n\n".format(ip_or_hostname,
                                                                   username, key_file_path, key_file_passphrase, port, key))

        log("\n")

        function(ip_or_hostname, username, key_file_path,
                 key_file_passphrase, port)
    else:
        print("\n\tPrivate Key: {} does not exist\n".format(key_file_path))
else:
    log('done')
