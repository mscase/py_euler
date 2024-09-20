#!/usr/bin/env python3 

SUMMARY="""Lattice Paths"""

"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

import math

# need to make 40 moves total, 20 right + 20 down

# bin_coefficient (n k) = ( n! / (k! * (n-k)!)

a = 20
b = 20
n = a + b
k = a

n_fac = math.factorial(40)
k_fac = math.factorial(20)
nk_fac = k_fac

print(int(n_fac / k_fac / nk_fac))

# also

print(int(math.comb(n, k)))
