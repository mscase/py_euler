import string

with open('p022_names.txt','r') as file:
    for line in file.readlines():
        names = line.rstrip().replace('"',"").split(',')
        names.sort()
total=0
for x in range(len(names)):
    name_sum = sum([string.ascii_lowercase.index(s)+1 for s in names[x].lower()])
    print (names[x], name_sum)
    total+= (x+1) * name_sum
print (total)
