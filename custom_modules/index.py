#! /usr/bin/env python3
import sys
import os
from CommandSender import sendCommand
from Tree import sendTree

ARG_COUNT = len(sys.argv)
ARGS = sys.argv


def cls(): return os.system('clear')


def log(arg):
    print("{0}\n".format(str(arg)))


"""
sendCommand: Sends a system command to the target host computer system, then outputs the results to standard out.
      @params ip:     The hostname or IP address of the target system
@params username:     A username from the system's accounts
@params password:     The user's password
 @params command:     The command to send to the system
    @params port:     The port to connect with; defaults to 30777

sendTree: Sends a system command to the target host computer system, then outputs the results to standard out.
      @params ip:     The hostname or IP address of the target system
@params username:     A username from the system's accounts
@params password:     The user's password
"""


def send():
    cls()
    sendCommand(ARGS[1], ARGS[2], ARGS[3], ARGS[4], ARGS[5])


if ARG_COUNT == 7:
    if ARGS[6].strip().lower() == "send":
        send()
    else:
        log("Done")
elif ARG_COUNT == 5:
    sendTree(ARGS[1], ARGS[2], ARGS[3], ARGS[4])
else:
    log('done')
