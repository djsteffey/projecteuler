def collatz(n):
    if n % 2 == 0:
        return n / 2
    return 3 * n + 1

largest = []
for i in range(1, 1000001):
    chain = []
    num = i
    chain.append(num)
    while num != 1:
        num = collatz(num)
        chain.append(num)
    if len(chain) > len(largest):
        largest = chain
        print('new largest', i, len(largest))
