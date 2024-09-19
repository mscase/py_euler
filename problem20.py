#!/usr/bin/python

import math

chars=(list(str(math.factorial(100))))
total=0
for x in chars:
    total+=int(x)

print (total)
