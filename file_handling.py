#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description ="Get input filename and write to it")
parser.add_argument('filename', help='Filename to write contents')

args = parser.parse_args()

print ("Enter text to write to file %s. Entering a new line will write contents to the file." % args.filename)
content = []
while True:
    input = raw_input()
    if not input:
        break;
    content.append("%s\n" % input)

with open(args.filename,'w') as f:
    f.writelines(content)
