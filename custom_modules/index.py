#! /usr/bin/env python3
from custom_modules.CommandSender import sendCommand
from custom_modules.TreeCommandSender import sendTree


def command(ip, username, password, command, port):
    sendCommand(ip, username, password, command, port)


def tree(ip, username, password, port):
    sendTree(ip, username, password, port)
