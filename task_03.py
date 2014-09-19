#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prompting inside a loop part 2"""

import data

PASSWORD = data.PASSWORD
ACCESS = False
NUM_GUESS = 3

# reread instructions, everything should depend on Access
while not ACCESS:
    GUESS = raw_input(
    "What is your password ({0} attempts left)? ".format(NUM_GUESS))
    print GUESS
    if GUESS == PASSWORD:
        print "Access granted!"
        ACCESS = True    
    else: 
	    NUM_GUESS -= 1
            if NUM_GUESS == 0:
                print "Access denied. Please try again later."
                break

#while NUM_GUESS > 0:
#    GUESS = raw_input(
#    "What is your password ({0} attempts left)? ").format(NUM_GUESS)
#    print GUESS
#    NUM_GUESS -= 1
#    if GUESS == PASSWORD:
#        print "Access granted!"
#        ACCESS = True
#        break
#	 if GUESS != PASSWORD:
#            ACCESS = False
#    else:
#        print "Access denied. Please try again later."
#        break