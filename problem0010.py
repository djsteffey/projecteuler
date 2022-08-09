import sympy

sum = 2
for i in range(3, 2000000, 2):
    if sympy.isprime(i):
        print('prime', i)
        sum += i
print(sum)