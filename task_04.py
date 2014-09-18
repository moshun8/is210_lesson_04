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
    DAILY_TOT = 0
    for INDIV_TRANS in DAY:  # break down into each number in list
        DAILY_TOT += INDIV_TRANS
    if DAILY_TOT < MINIMUM:  # too much indentation before
        MINIMUM = DAILY_TOT
    elif DAILY_TOT > MAXIMUM:
        MAXIMUM = DAILY_TOT
TOTAL = DAILY_TOT