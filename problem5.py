#!/usr/bin/env python3

SUMMARY="""Smallest Multiple"""

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?
"""

#max_test=10 #2520
max_test=20
# ignoring 1, all numbers are divisible by 1
test_values = [x for x in range(2,max_test+1)]
print (test_values)

num=max_test
while True:
    found = True
    for val in test_values:
        if num % val != 0:
           found = False
           break     
    if found:
        break
    num+=max_test

print (num)
