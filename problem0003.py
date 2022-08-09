import math

def findFactors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return factors

num = 600851475143
factors = findFactors(num)
primes = []
for factor in factors:
    if len(findFactors(factor)) == 2:
        primes.append(factor)
print(max(primes))