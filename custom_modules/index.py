#! /usr/bin/env python3
from custom_modules.CommandSender import sendCommand
from custom_modules.TreeCommandSender import sendTree


"""
command: Sends a system command to the target host computer system, then outputs the results to standard out.
      @params ip:     The hostname or IP address of the target system
@params username:     A username from the system's accounts
@params password:     The user's password
 @params command:     The command to send to the system
    @params port:     The port to connect with; defaults to 30777
"""


def command(ip, username, password, command, port):
    sendCommand(ip, username, password, command, port)


"""
tree: Sends the tree command to the target host computer system, then outputs the results to standard out.
      @params ip:     The hostname or IP address of the target system
@params username:     A username from the system's accounts
@params password:     The user's password
    @params port:     The port to make the connection
"""


def tree(ip, username, password, port):
    sendTree(ip, username, password, port)
