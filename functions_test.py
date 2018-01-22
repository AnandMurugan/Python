#!/usr/bin/env python

def print_message(message, count):
    while count > 0:
        print (message)
        count = count - 1


message = raw_input("Please enter a message to echo ")
string_count = raw_input("Please enter number of times to print the message ") 

if string_count:
    count = int(string_count)
else:
    count = 1

print_message(message, count)
