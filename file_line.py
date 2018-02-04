#!/usr/bin/env python

import argparse
import os

parser = argparse.ArgumentParser(description="Program to retrieve a specified line from a file")
parser.add_argument('filename',help='Specify a File name to read contents.')
parser.add_argument('--linenumber', type=int, help='line number in the file to return')

args = parser.parse_args()

try:
    f = open(args.filename, 'r')
except IOError:
    print("IOError: %s doesn't exist" % (args.filename))
else:
    with f:
        lines=f.readlines()
        line_to_return = args.linenumber
        if len(lines)<line_to_return:
            print ("Line number %s not found" % (line_to_return))
        else:
            print lines[line_to_return-1].strip()
