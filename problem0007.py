def isPrime(num):
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

primes = []

num = 2
while True:
    if isPrime(num):
        primes.append(num)
        print(len(primes), 'found prime', num)
        if len(primes) == 10001:
            break
    num += 1

print(primes[-1])