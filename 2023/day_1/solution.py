file = open('input.txt', 'r')
lines = file.readlines()

num_words = "one two three four five six seven eight nine".split()

def get_first(line):
    for i in range(len(line)):
        for j in range(len(num_words)):
            num_word = num_words[j]
            chars = line[i:i+len(num_words[j])]
            if ( chars == num_word):
                return j+1
        if line[i].isdigit():
            return int(line[i])

def get_last(line):
    rev_line = line[::-1]
    rev_num_words = [word[::-1] for word in num_words]
    for i in range(len(rev_line)):
        for j in range(len(rev_num_words)):
            num_word = rev_num_words[j]
            chars = rev_line[i:i+len(rev_num_words[j])]
            if ( chars == num_word):
                return j+1
        if rev_line[i].isdigit():
            return int(rev_line[i])

total = 0
for line in lines:
    total += get_first(line)*10 + get_last(line)

print(total)