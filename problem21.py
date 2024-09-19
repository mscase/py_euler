
amicables=set()

for a in range(1,10001):
    div_a=[1]
    for y in range(2,a):
        if a % y == 0:
            div_a.append(y)
    print (f'a={a} div_a={div_a}')

    div_a_sum = sum(div_a)
    b = div_a_sum

    div_b = [1]
    for y in range(2,b):
        if b % y == 0:
            div_b.append(y)

    print (f'div_b={div_b}')
    div_b_sum = sum(div_b)
    if div_a_sum == b and div_b_sum == a:
        if a != b:
            amicables.add(a)
            amicables.add(b)
print (sum(amicables))
