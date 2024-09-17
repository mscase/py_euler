#!/usr/bin/env python3

import math

SUMMARY="""Largest prime factor"""

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

#num=13195
num=600851475143

primes = set([2])
factors = set()

for i in range(3, int(math.sqrt(num)),2):
    isprime = True
    for p in primes:
        if i % p == 0:
            isprime = False
            break
    if isprime:
        primes.add(i)
        if num % i == 0: 
             factors.add(i)
             num = int(num/ i)
    if num == 1:
        break

print (sorted(factors))
print (sorted(factors)[-1])
