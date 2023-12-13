blocks = [x.split('\n') for x in open('input.txt').read().split("\n\n")]


def print_blocks(blocks):
    for block in blocks:
        for line in block:
            print(line)
        print('')


def get_column(j, block):
    column = []
    for line in block:
        column.append(line[j])
    return column


def vert(block):
    for i in range(len(block[0])-1):
        left_i = i
        right_i = i+1
        reflective = True
        while left_i >= 0 and right_i < len(block[0]):
            if not get_column(left_i, block) == get_column(right_i, block):
                reflective = False
                break
            left_i -= 1
            right_i += 1
        
        if reflective == True:
            return i+1
    return reflective

def horizon(block):
    for i,line in enumerate(block[:-1]):
        top_i = i
        bottom_i = i+1
        reflective = True
        while top_i >= 0 and bottom_i < len(block):
            if not block[top_i] == block[bottom_i]:
                reflective = False
                break
            top_i -= 1
            bottom_i += 1
        
        if reflective == True:
            return i+1
        
    return reflective

def bin(line):
    bin_line = []
    for char in line:
        if char == '#':
            bin_line.append(1)
        else:
            bin_line.append(0)
    return bin_line

def diff_lines(line_1,line_2):
    diff = []
    for i in range(len(line_1)):
        diff.append(abs(line_1[i] - line_2[i]))


    return diff

def horizon_diff(i, block):
    diff = []
    top_i = i
    bottom_i = i+1
    while top_i >= 0 and bottom_i < len(block):
        top_line = bin(block[top_i])
        bottom_line = bin(block[bottom_i])
        diff.append(diff_lines(top_line, bottom_line))
        top_i -= 1
        bottom_i += 1
    return diff

def new_horizon(block):
    for i in range(len(block)):
        diff = horizon_diff(i, block)
        mistakes = sum([sum(x) for x in diff])
        if mistakes == 1:
            return i+1
    return 0
        
def vert_diff(i, block):
    diff = []
    left_i = i
    right_i = i+1
    while left_i >= 0 and right_i < len(block[0]):
        top_line = bin(get_column(left_i, block))
        bottom_line = bin(get_column(right_i, block))
        diff.append(diff_lines(top_line, bottom_line))
        left_i -= 1
        right_i += 1
    return diff

def new_vert(block):
    for i in range(len(block[0])):
        diff = vert_diff(i, block)
        mistakes = sum([sum(x) for x in diff])
        if mistakes == 1:
            return i+1
    return 0


total = 0
for block in blocks:
    vert_lof = vert(block)
    horizon_lof = horizon(block)
    total += new_horizon(block)*100
    total += new_vert(block)
                

print(total)


# print(horizon_diff(2, blocks[0]))