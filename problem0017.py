map = {}
map[1] = 'one'
map[2] = 'two'
map[3] = 'three'
map[4] = 'four'
map[5] = 'five'
map[6] = 'six'
map[7] = 'seven'
map[8] = 'eight'
map[9] = 'nine'
map[10] = 'ten'
map[11] = 'eleven'
map[12] = 'twelve'
map[13] = 'thirteen'
map[14] = 'fourteen'
map[15] = 'fifteen'
map[16] = 'sixteen'
map[17] = 'seventeen'
map[18] = 'eighteen'
map[19] = 'nineteen'

map2 = {}
map2[1] = 'teen'
map2[2] = 'twenty'
map2[3] = 'thirty'
map2[4] = 'forty'
map2[5] = 'fifty'
map2[6] = 'sixty'
map2[7] = 'seventy'
map2[8] = 'eighty'
map2[9] = 'ninety'

def convertToWords(num):
    word = ''
    if num >= 1000:
        word += map[num//1000] + ' thousand '
        num = num % 1000
    if num >= 100:
        word += map[num//100] + ' hundred '
        num = num % 100
    if num > 0 and word != '':
        word += 'and '
    if num > 0 and num < 20:
        word += map[num]
        num = 0
    elif num >= 20:
        word += map2[num//10] + '-'
        num = num % 10
    if num > 0:
        word += map[num]
    return word

def countLetters(word):
    count = 0
    for c in word:
        if c != ' ' and c != '-':
            count += 1
    return count

sum = 0
for i in range(1, 1001):
    words = convertToWords(i)
    letters = countLetters(words)
    print(i, words, letters)
    sum += letters

print(sum)