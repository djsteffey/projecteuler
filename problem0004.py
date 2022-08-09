def isPalindrom(num):
    num = str(num)
    rev = num[::-1]
    if num == rev:
        return True
    return False

palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if isPalindrom(num):
            palindromes.append(num)

print(max(palindromes))
