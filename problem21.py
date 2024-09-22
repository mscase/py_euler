#!/usr/bin/env python3

SUMMARY="""Amicable Numbers"""

"""
Let d(n) be defined as the sum of proper divisors n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.  
The proper divisors of 284 are 1, 2, 4, 71 and 142; so (284) = 200.

Evaluate the sum of all the amicable numbers under 10000.
"""

amicables=set()

for a in range(1,10001):
    div_a=[1]
    # range limit from problem 12
    for y in range(2,int(a**0.5)+1):
        if a % y == 0:
            div_a.append(y)
            div_a.append(int(a/y))
    #print (f'a={a} div_a={div_a}')

    div_a_sum = sum(div_a)
    b = div_a_sum

    div_b = [1]
    for y in range(2,int(b**0.5)+1):
        if b % y == 0:
            div_b.append(y)
            div_b.append(int(b/y))
    #print (f'div_b={div_b}')
    div_b_sum = sum(div_b)
    if div_a_sum == b and div_b_sum == a:
        if a != b:
            amicables.add(a)
            amicables.add(b)
print (sum(amicables))
