#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prompting inside a loop part 2"""

import data

PASS = data.PASSWORD
ACCESS = False
NUM_GUESS = 3

while not ACCESS:
    GUESS = raw_input("What is your password ({0} attempts left)? "
    ).format(NUM_GUESS)
    if GUESS == PASS:
        print "Access granted!"
        ACCESS = True
	elif GUESS != PASS:
        NUM_GUESS -= 1
        ACCESS = False
    elif NUM_GUESS == 0:
        print "Access denied. Please try again later."
        break
