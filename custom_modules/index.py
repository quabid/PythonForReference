#! /usr/bin/env python3
from custom_modules.CommandSender import sendCommandKey, sendCommandPassword
from custom_modules.TreeCommandSender import sendTreePass, sendTreeKey
from custom_modules.FileValidator import fileExists


"""
    sendCommandPassword: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params password:           The user's password
    @params command:            The command to send to the system
    @params port:               The port to connect with; defaults to 30777
"""


def commandPassword(ip, username, password, command, port):
    sendCommandPassword(ip, username, password, command, port)


"""
    sendCommandKey: Sends a system command to the target host computer system, then outputs the results to standard out.
    @params ip:                 The hostname or IP address of the target system
    @params username:           A username from the system's accounts
    @params key_file_path:      The absolute path to the private key file to access the host
    @params pass_phrase         The passphrase for the private key
    @params command:            The command to send to the system
    @params port:               The port to connect with; defaults to 30777
"""


def commandKey(ip, username, key_file_path, pass_phrase, command, port):
    sendCommandKey(ip, username, key_file_path, pass_phrase, command, port)


"""
tree: Sends the tree command to the target host computer system, then outputs the results to standard out.
@params ip:                     The hostname or IP address of the target system
@params username:               A username from the system's accounts
@params password:               The user's password
@params port:                   The port to make the connection
"""


def treePass(ip, username, password, port):
    sendTreePass(ip, username, password, port)


"""
tree: Sends the tree command to the target host computer system, then outputs the results to standard out.
@params ip:                     The hostname or IP address of the target system
@params username:               A username from the system's accounts
@params key_file_path:          The absolute path to the private key file to access the host
@params pass_phrase             The passphrase for the private key
@params port:                   The port to make the connection
"""


def treeKey(ip, username, key_file_path, pass_phrase, port):
    sendTreeKey(ip, username, key_file_path, pass_phrase, port)
