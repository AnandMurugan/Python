#!/usr/bin/env python

def print_message(message, count):
    while count > 0:
        print (message)
        count = count - 1


message = raw_input("Please enter a message to echo ")
count = input("Please enter number of times to print the message ")

if not count:
    count = 1

print_message(message, count)
print ("You entered : %s " % (message))
