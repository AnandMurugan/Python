#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description="Program to retrieve a specified line from a file")
parser.add_argument('filename',help='Specify a File name to read contents.')

args = parser.parse_args()

with open(args.filename,'r') as f:
    lines=f.readlines()
    print lines

print('EOF')
