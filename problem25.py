#!/usr/bin/env python3

SUMMARY="""1000-digit Fibonacci Number"""

"""
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_n-1 + F_n-2 where F_1 = 1 and F_2 = 1

Hence the first 12 terms will be:

F_1 = 1
F_2 = 1
F_3 = 2
F_4 = 3
F_5 = 5
F_6 = 8
F_7 = 13
F_8 = 21
F_9 = 34
F_10 = 55
F_11 = 89
F_12 = 144 

The 12th term, F_12 is hte first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

print ('first 12 terms')
idx = 3
N_1 = 1
N_2 = 1
while True:
    current = N_1 + N_2
    N_2 = N_1
    N_1 = current
    print (idx, current, len(str(current)))
    if len(str(current)) >= 3:
        break
    idx+=1
    
print ('\nsolution')
idx = 3
N_1 = 1
N_2 = 1
while True:
    current = N_1 + N_2
    N_2 = N_1
    N_1 = current
    #print (idx, current, len(str(current)))
    if len(str(current)) >= 1000:
        break
    idx+=1
print (idx)
    
    
