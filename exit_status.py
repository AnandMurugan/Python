#!/usr/bin/env python2

from argparse import ArgumentParser
from subprocess import check_output,CalledProcessError,STDOUT
from os import kill
from sys import exit

parser = ArgumentParser(description="Program to scan free up a specified port")
parser.add_argument('port_number', help="Specify a port number to perform free action")

args = parser.parse_args()

try:
    output = check_output(
        ['lsof', '-i4TCP:%s' % args.port_number, '-n'],
        stderr=STDOUT
    )
except OSError as error:
    print("OSError %s " % error)
    output = error
except CalledProcessError as e:
    print("No process is listening on port %s" % args.port_number)
    exit(e.returncode)
else:
    lines = output.splitlines()
    listening = None
    for line in lines:
        if "LISTEN" in line:
            listening = line
            break;

    if listening:
        process_id = listening.split()[1]
        print("Killing process with process id %s " % process_id)
        kill(int(process_id), 9)
    else:
        print("No process is listening on port %s" % args.port_number)
        exit(1)
