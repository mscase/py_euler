#!/usr/bin/env python3

import math
import libs.sieve as sieve
import time

SUMMARY="""Problem 7: 10001st prime"""

# start a list of primes
primes=sieve.sieve(100)

MAX_NUM=10001

x=101
start_time = time.time()
while len(primes) < MAX_NUM:
    isprime = True
    for p in primes:
        if x % p == 0:
            isprime = False
            break
    if isprime:
        primes.append(x)
    x+=2        

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
print ("10001st prime is {}".format(primes[-1]))
