# Using readlines()
file1 = open('input1.txt', 'r')
Lines = file1.readlines()


def wordcheck(i, _list):
    words = ['zero',
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine']

    for j in range(len(words)):
        if _list[i:i+len(words[j])] == list(words[j]):
            return j
    return False
count = 0
sum = 0
# Strips the newline character
for line in Lines:
    count += 1
    line = list(line.strip())
    first = -1
    last = -1
    for i in range(len(line)):
        num = wordcheck(i, line)
        if num != False:
            last = num
            if first == -1:
                first = num
        if (line[i] in ['0','1','2','3','4','5','6','7','8','9']):
            last = int(line[i])
            if first == -1:
                first = int(line[i])
    sum+=first*10+last
print(sum)

