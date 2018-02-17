#!/usr/bin/env python2

import argparse
import subprocess
from os import kill

parser = argparse.ArgumentParser(description="Program to scan free up a specified port")
parser.add_argument('port_number', help="Specify a port number to perform free action")

args = parser.parse_args()

try:
    output = subprocess.check_output(
        ['lsof', '-i4TCP:%s' % args.port_number, '-n'],
        stderr=subprocess.STDOUT
    )
except OSError as error:
    print("OSError %s " % error)
    output = error
except subprocess.CalledProcessError as e:
    print("No process is running on port %s. It is available." % args.port_number)
else:
    lines = output.splitlines()
    for line in lines:
        if "LISTEN" in line:
            process_id = line.split()[1]
            print("Killing process with process id %s " % process_id)
            kill(int(process_id), 9)
    print("Port %s is available." % args.port_number)
