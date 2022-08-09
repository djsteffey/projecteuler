import math

def findFactors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return factors

def computeTriangle(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

num = 1
while True:
    triangle = computeTriangle(num)
    factors = findFactors(triangle)
    print(num, triangle, len(factors))
    if len(factors) >= 500:
        break
    num += 1