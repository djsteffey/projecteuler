num = 20
while True:
    if num % 1000000 == 0:
        print('checking', num)
    result = True
    for i in range(1, 21):
        if num % i != 0:
            result = False
            break
    if result:
        print(num)
        break
    num += 1

        
