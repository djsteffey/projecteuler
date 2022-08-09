sumSquares = 0
for i in range(1, 101):
    sumSquares += (i * i)

squareSums = 0
for i in range(1, 101):
    squareSums += i
squareSums = squareSums * squareSums

diff = squareSums - sumSquares

print(diff)