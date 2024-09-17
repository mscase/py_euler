#!/usr/bin/env python3

SUMMARY="""Largest palindrome product"""

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

#print (product, len(str(product)))
# str[::-1]
largest = 0
for x in range(999,99,-1):
    for y in range(x,99,-1):
        product=x*y
        prod_str = str(product)
        prod_str_rev = str(product)[::-1]
        if prod_str == prod_str_rev:
            if product > largest:
                largest = product

print (largest)
