#!/usr/bin/env python

import argparse
import os

parser = argparse.ArgumentParser(description="Program to retrieve a specified line from a file")
parser.add_argument('filename', help='Specify a File name to read contents.')
parser.add_argument('line_number', type=int, help='line number in the file to return')

args = parser.parse_args()

try:
    f = open(args.filename, 'r')
    with f:
        lines = f.readlines()
        line = lines[args.line_number - 1]
except IndexError:
    print("Line number %s not found" % (args.line_number))
except IOError:
    print("IOError: %s doesn't exist" % (args.filename))
else:
    print line.strip()
