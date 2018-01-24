#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description ="Get input filename and write to it")
parser.add_argument('filename', help='Filename to write contents')

args = parser.parse_args()
print(args)

with open(args[1],'w') as f:
    f.readlines()
