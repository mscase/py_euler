#!/usr/bin/env python3

SUMMARY="""Names Scores"""

"""
Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 times 53 = 49714.
What is the total of all the name scores in the file?


"""

import string

with open('p022_names.txt','r') as file:
    for line in file.readlines():
        names = line.rstrip().replace('"',"").split(',')

names.sort()

total=0
for x in range(len(names)):
    name_sum = sum([string.ascii_lowercase.index(s)+1 for s in names[x].lower()])
    #print (names[x], name_sum)
    total+= (x+1) * name_sum
print (total)
