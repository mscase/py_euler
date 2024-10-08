#!/usr/bin/env python3 

SUMMARY="""Even Fibonacci numbers"""

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


"""

x=1
y=2
z=0
sum=0

max_num=4*1000*1000

while y < max_num:
    if y % 2 == 0:
        sum+=y
    z=x
    x=y
    y=z+y

print (sum)
