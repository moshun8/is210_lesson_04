#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Looping Math"""

import data
TRAN = data.TRANSACTIONS
TOTAL = 0
MINIMUM = 0
MAXIMUM = 0

# Total will have to = all the individual totals

for DAY in TRAN:  # break down list to elements/days    
    DAY_TOT = 0
    for INDIV_TRANS in DAY:  # break down into each number in a day
        DAY_TOT += INDIV_TRANS
        if DAY_TOT < MINIMUM:
            MINIMUM = TOTAL
        elif DAY_TOT > MAXIMUM:
             MAXIMUM = TOTAL
print MINIMUM
print MAXIMUM