#!/usr/bin/env python

def readuserinput():
    msg = raw_input("Please enter a message to echo ")
    return (msg)

message = readuserinput()
print ("You entered : %s " % (message))
