#!/usr/bin/env python

users = [{'admin': True, 'active': True, 'name': 'Kavin'},
         {'admin': False, 'active': True, 'name': 'Tom'},
         {'admin': True, 'active': False, 'name': 'Jerry'},
         {'admin': False, 'active': False, 'name': 'Mickey'},
         {'admin': True, 'active': True, 'name': 'Popeye'}]
line_number = 1
for user in users:
    if user['admin'] and user['active']:
        print ("%s (ADMIN) - ACTIVE %s " % (line_number, user['name']))
    elif user['active']:
        print ("%s ACTIVE %s " % (line_number, user['name']))
    elif user['admin']:
        print ("%s (ADMIN) %s " % (line_number, user['name']))
    else:
        print ("%s %s " % (line_number, user['name']))
    line_number += 1
