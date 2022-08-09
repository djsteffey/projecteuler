# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# start sum at 0
sum = 0

# loop though all whole numbers less than 1000
for i in range(1000):
    # check if divisible by 3
    if i % 3 == 0:
        # add to sum
        sum += i
    # else if divisible by 5
    elif i % 5 == 0:
        # add to sum
        sum += i

# complete
print(sum)