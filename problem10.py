#!/usr/bin/env python3

SUMMARY="""Summation of Primes"""

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math
import libs.sieve as sieve

EXAMPLE_MAX_NUM=10
MAX_NUM=2000000

#primes=sieve.sieve_prime_list(EXAMPLE_MAX_NUM)
primes=sieve.sieve(EXAMPLE_MAX_NUM)
print ("Sum of primes below {} is: {}".format(EXAMPLE_MAX_NUM, sum(primes)))

primes=sieve.sieve(MAX_NUM)
print ("Sum of primes below {} is: {}".format(MAX_NUM, sum(primes)))

