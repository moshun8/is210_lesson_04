#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1: Analyze a string"""

import data
print data.SHAKESPEARE

POEM = data.SHAKESPEARE

MAXIMUM_WORDS = 0.0
MINIMUM_WORDS = 10000.0
AVERAGE_WORDS = 0.0
NUM_CRISPIAN = 0.0

LINES = POEM.split('\n') # Splits POEM into lines
TOTAL_WORDS = 0.0
TIMES_CRISPIAN = 0.0

for LINE in LINES:
    WORDS = LINE.split() # Splits lines into words
    SIZE = len(WORDS) # Finds number of words in a line
    TOTAL_WORDS += SIZE # Adds up number of words in whole doc
    AVERAGE_WORDS = float(TOTAL_WORDS)/float(len(LINES))
    if SIZE > MAXIMUM_WORDS: MAXIMUM_WORDS = SIZE
    if SIZE < MINIMUM_WORDS: MINIMUM_WORDS = SIZE
    if "Crispian" in LINE: NUM_CRISPIAN += 1

print MAXIMUM_WORDS, MINIMUM_WORDS, TOTAL_WORDS, AVERAGE_WORDS, NUM_CRISPIAN


# Need a count variable and accumulator variable
# if MAXIMUM_WORDS > accumulator:
#	MAXIMUM_WORDS = accumulator"""

