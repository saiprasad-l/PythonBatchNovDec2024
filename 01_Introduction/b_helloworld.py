#!/usr/bin/python3
"""
Purpose : Basic PEP 8 Guidelines
    PEP - Python Enhancement proposal
    coding style guide

This is a Doc string
"""

# print "Hello World"  Python2

print ("Hello World!")


def wishes(name):
    wish = "How are you {0}?" . format(name)
    print(wish)

wishes("Prasad")