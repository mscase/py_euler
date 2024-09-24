#!/usr/bin/env python3

SUMMARY="""Lexicographic Permutations"""

"""
A permutation is an ordered arrangement of objects.  For example, 3124 is one possible permutation of the digits 1, 2, 3, and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographics order.  The lexicographics permutations of 0, 1, and 2 are: 

012, 021, 102, 120, 201, 210

What is the millionth lexicographics permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?
"""
# 0123456789
# 0123456798
# 0123456879
# 0123456897
# 0123456978

import time
from itertools import permutations

digits = [0,1,2,3,4,5,6,7,8,9]

start = time.time()
permutations = list(permutations(digits))
end = time.time()
print(''.join(map(str,permutations[999999])))
print(f'permutations method took : {end - start:.4f}')

# eulers method
import math

target = 1000000
answer = []

start = time.time()
for n in range(9,0,-1):
    n_f = math.factorial(n)
    idx = target // n_f
    remainder = target % n_f # aka remainder
    if remainder == 0:
        idx-=1
        remainder = target - (n_f * idx)
    target = remainder
    answer.append(digits.pop(idx))
answer.append(digits.pop())
end = time.time()
print (''.join(map(str,answer)))
print(f'FNS method took : {end - start:.6f}')
