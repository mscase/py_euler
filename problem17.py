#!/usr/bin/env python3

SUMMARY="""Number Letter Counts"""

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.  For example, 342 (three hundred and forty-two) contains 23 letters and 
115 (one hundred and fifteen) contains 20 letters.  The use of 'and' when writing out numbers is in compliance with 
British usage.
"""

ones_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens_dict = {
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def ones(number):
    if number < 20:
        num = number
    else:
        num = number % 10
    if num == 0:
        return 0
    s1 = ones_dict[num]
    return len(s1)

def tens(number):
    if number < 20:
        return 0 
    num = (number // 10) * 10
    s1 = tens_dict[num]
    return len(s1)

def hundreds(number):
    if number < 100:
        return 0
    num = number // 100
    s1 = ones_dict[num]
    s1+='hundred'
    if number % 100 != 0:
        s1+='and'
    return len(s1)

def test_342():
    num = 342
    l_total =0
    l_total += hundreds(num)
    num = num % 100
    l_total += tens(num)
    l_total += ones(num)
    print(f'342 = {l_total}')
    
def test_115():
    num = 115
    l_total =0
    l_total += hundreds(num)
    num = num % 100
    l_total += tens(num)
    l_total += ones(num)
    print(f'115 = {l_total}')
    

test_342()
test_115()

thousand_len = len("onethousand")
total = thousand_len
for n in range(1, 1000):
    num = n
    l_total = 0
    l_total += hundreds(num)
    num = num % 100
    l_total += tens(num)
    l_total += ones(num)
    total+=l_total
print (total)
