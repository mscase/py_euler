#!/usr/bin/env python3

SUMMARY="""Longest Collatz Sequence"""

"""
The following iterative sequence is defined for the set of positive integers:

n to n/2 (n is even)
n to 3n + 1( n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 to 40 to 20 to 10 to 5 to 16 to 8 to 4 to 2 to 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

longest_sequence = 0
longest_n = 0
for n in range(2, 1000000):
    start_n = n
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = (n * 3) + 1
        sequence.append(n)
    if len(sequence) > longest_sequence:
        longest_sequence = len(sequence)
        longest_n = start_n

print (longest_n)
