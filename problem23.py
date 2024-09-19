#perfects=[]
#for x in range(2, 28124, 2):
#    div_x=[1]
#    for y in range(2,x):
#        if x % y == 0:
#            div_x.append(y)
#
#    if x == sum(div_x): 
#        print (x, div_x, sum(div_x))
#        perfects.append(sum(div_x))
perfects = [6, 28, 496, 8128]
print (perfects)

abundants = []
for x in range(2, 28124):
    div_x=[1]
    for y in range(2,x):
        if x % y == 0:
            div_x.append(y)
    if sum(div_x) > x:
        abundants.append(x)
print (abundants)

all_nums = set([x for x in range(1,28124)])
cannots = set()
for n in range(1,28124):
    print (n)
    for a in abundants:
        cannot = True
        for b in abundants:
            if a + b == n:
                cannot = False
                break
        if cannot:
            cannots.add(n)

print (cannots)
print (sum(cannots))

