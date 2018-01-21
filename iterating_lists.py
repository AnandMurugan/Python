#!/usr/bin/env python

users = [{'admin': True, 'active': True, 'name': 'Kavin'},
         {'admin': False, 'active': True, 'name': 'Tom'},
         {'admin': True, 'active': False, 'name': 'Jerry'},
         {'admin': False, 'active': False, 'name': 'Mickey'},
         {'admin': True, 'active': True, 'name': 'Popeye'}]

for user in users:
    if user['admin'] and user['active']:
        print ("(ADMIN) - ACTIVE %s " % (user['name']))
    elif user['active']:
        print ("ACTIVE %s " % (user['name']))
    elif user['admin']:
        print ("(ADMIN) %s " % (user['name']))
    else:
        print ("%s " % (user['name']))
