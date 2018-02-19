#!/usr/bin/env python

import requests
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description='Program to download a url to JSON or HTML')
parser.add_argument('url', help='Please specify a url to download contents from...')
parser.add_argument('filename', help='Destination file name to write contents to.')
parser.add_argument('--format',
                    default='html',
                    choices=['json','html'],
                    help='destination file format.')
args = parser.parse_args()

res = requests.get(args.url)
if res.status_code >= 400:
    print("Error: connecting to url, status code %s" % res.status_code)
    sys.exit(1)

if args.format == 'json':
    try:
        content = res.json()
        print("writing contents in json format...")
    except ValueError:
        print("Value error in decoding url contents to json")
        sys.exit(1)
else:
    content = res.text.encode('utf-8')
    
with open(args.filename + '.' + args.format,'w') as f:
    f.writelines(content)
    print("contents written in %s format to file %s " % (args.format, args.filename))
