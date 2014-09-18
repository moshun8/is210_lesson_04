#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prompting inside a loop part 1"""

VALID = False
INPUT_NUM = 0
FACTORIAL = 1
PRODUCT = 1

while not VALID:
    INPUT_NUM = int(raw_input("Enter a number >> "))
    if INPUT_NUM > 0:
        VALID = True
    elif INPUT_NUM < 0:
        print "Invalid number: Please enter a number greater than zero."
    else:
        VALID = False

while FACTORIAL <= INPUT_NUM:
    PRODUCT = PRODUCT * FACTORIAL
    FACTORIAL = FACTORIAL + 1

print "The factorial of {0} is {1}.".format(INPUT_NUM, PRODUCT)