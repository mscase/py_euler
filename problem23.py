#!/usr/bin/env python3

SUMMARY="""Non-Abundant Sums"""

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# don't need this
perfects = [6, 28, 496, 8128]
print (perfects)

abundants = []
for x in range(2, 28124):
    div_x={1}
    for y in range(2,int(x**0.5)+1):
        if x % y == 0:
            div_x.add(y)
            div_x.add(int(x/y))
    if sum(div_x) > x:
        abundants.append(x)
#print (abundants)
print (f'{len(abundants)} abundant numbers')
num_abundants = len(abundants)

all_nums = set([x for x in range(1,28124)])
double_abundants = {num * 2 for num in abundants}
all_nums = all_nums - double_abundants

cannots = set()
for num in all_nums:
    cannot = True
    limited_set = {x for x in abundants if x <= num}
    for t_val in limited_set:
        if (num - t_val in limited_set):
            cannot = False
            break
    if cannot:
        cannots.add(num)

#print (cannots)
print (sum(cannots))

