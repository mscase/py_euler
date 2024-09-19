import math

# bin_coeffienct (n k) = ( n! / (k! * (n-k)!)

a = 20
b = 20
n = a + b
k = a

n_fac = math.factorial(40)
k_fac = math.factorial(20)
nk_fac = k_fac

print(n_fac / k_fac / nk_fac)
