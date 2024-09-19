#!/usr/bin/env python3

SUMMARY="""Multiples of 3 or 5"""

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000
"""

import time
start = time.time()
A = set([i for i in range(0,1000,3)])
B = set([i for i in range(0,1000,5)])
end = time.time()
print (sum(A | B))
print (f'with sets = {end - start}')

total = 0
start = time.time()
for x in range(0, 1000):
    if (x % 3 == 0 or x % 5 == 0):
        total += x
end = time.time()
print (total)
print (f'for loop = {end - start}')
