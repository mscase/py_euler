#!/usr/bin/env python3

SUMMARY="""Sum square difference"""

"""
The sum of the squares of the first ten natural numbers is
1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is
(1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n=100

print('method 1')
sum_of_squares=sum([x*x for x in range(1,n+1)])
sum_n=sum([x for x in range(1,n+1)])
square_of_sum=sum_n*sum_n
print (square_of_sum - sum_of_squares)

print ('method2')
#sum_of_squares = n*(n+1)*((2*n)+1)/6
#      sum_of_n = n*(n+1)/2
sum_of_sq2 = int(100 * ( 101 ) * ( 201 ) / 6)
sum_of_n2 = int(100 * 101 / 2)

print ((sum_of_n2 * sum_of_n2) - sum_of_sq2)
