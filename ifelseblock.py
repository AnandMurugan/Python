#!/usr/bin/env python

user = { 'admin': True, 'active': True, 'name': 'Kevin'}

for key, value in user.items():
    if key is 'admin' and value is True:
        print ("User is admin")


