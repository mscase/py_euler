#!/usr/bin/env python3

SUMMARY="""Power Digit Sum"""

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

#power=15
power=1000

num = 2**power
total_sum = sum(int(c) for c in str(num))
print (f'sum of digits in {num} = {total_sum}')
