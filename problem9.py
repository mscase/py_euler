#!/usr/bin/env python3 

import math

SUMMARY="""Special Pythagorean Triplet"""

"""
A Pythagorean triplet is a set of three natural numbers, a > b > c, for which
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly on Pythagorean triplet for which a + b + c = 1000.  

Find the product abc.
"""

# a^2 + b^2 = c^2
# a + b + c = 1000
# product abc
prod = 0
for a in range (0, 1000):
    for b in range (a+1, 1000):
        c = math.sqrt((a*a) + (b*b))
        if (a + b + c) == 1000:
            prod = int(a * b * c)
print(prod)
