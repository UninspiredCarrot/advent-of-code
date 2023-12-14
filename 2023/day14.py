import time

platform = open('example.txt').read().split("\n")


def view(platform):
    for line in platform:
        print(line)

def get_column(j, platform):
    column = []
    for line in platform:
        column.append(line[j])
    return column


def move_col(column, reverse):
    square_pos = [i for i in range(len(column)) if column[i] == '#']
    square_pos.append(None)
    new_column = []
    start = 0
    for pos in square_pos:
        sub_column = column[start:pos]
        zero_num = sub_column.count('O')
        dot_num = sub_column.count('.')
        if reverse:
            new_column.extend(['.']*dot_num)
            new_column.extend(['O']*zero_num)
        else:
            new_column.extend(['O']*zero_num)
            new_column.extend(['.']*dot_num)
        if pos != None:
            new_column.append('#')
            start = pos+1
    return new_column


def calc(platform):
    total = 0
    for i in range(len(platform[0])):
        column = get_column(i, platform)
        for j, rock in enumerate(column):
            if rock == 'O':
                total += len(column)-j
    return total

cache = {}
def move_plat(platform, move_line, type, reverse=False):
    key = (''.join([''.join(x) for x in platform]),move_line, type, reverse)
    if key in cache:
        return cache[key]
    new_platform = []

    if type == 'column':
        temp_platform = []
        for i in range(len(platform[0])):
            line = get_column(i, platform)
            moved_line = move_line(line, reverse)
            temp_platform.append(moved_line[::-1])
            new_platform = list(zip(*temp_platform))[::-1]
    else:
        for i in range(len(platform[0])):
            line = platform[i]
            moved_line = move_line(line, reverse)
            new_platform.append(moved_line)

    cache[key] = new_platform
    return new_platform
    
    
    

spin_cache = {}
def spin(num_cycles, platform, start_time):
    new_platform = platform
    for i in range(num_cycles): 
        new_platform = move_plat(new_platform, move_col, 'column')
        # view(new_platform)
        # print('')
        new_platform = move_plat(new_platform, move_col, 'row')
        # view(new_platform)
        # print('')
        new_platform = move_plat(new_platform, move_col, 'column', reverse=True)
        # view(new_platform)
        # print('')
        new_platform = move_plat(new_platform, move_col, 'row', reverse=True)
        # view(new_platform)
        # print('\n')
        total = calc(new_platform)

        if total in spin_cache:
            spin_cache[total]['list'].append(i)
            if len(spin_cache[total]['list']) > 3:
                diff = spin_cache[total]['list'][-1] - spin_cache[total]['list'][-2]
                if diff in spin_cache[total]['diffs']:
                    spin_cache[total]['diffs'].remove(diff)
                spin_cache[total]['diffs'].append(diff)
        else:
            spin_cache[total] = {'list': [i], 
                                'diffs': []}
            

        # print([f'{key}: {spin_cache[key]["diffs"]}' for key in spin_cache])

            # print([f'{key}: {spin_cache[key]["diffs"]}' for key in spin_cache])
            # print([f'{key}: {spin_cache[key]["list"]}' for key in spin_cache if spin_cache[key]["list"][-1] == 13])
    return new_platform

start_time = time.time()
new_platform = spin(1000, platform, start_time)

# for key in spin_cache:
#     if (100000000 - spin_cache[key]['list'][-1])%7==0:
#         # print(spin_cache[key])
#         print(key)
c = 0
complete_answer = 0
for key in spin_cache:
    reps = sum(spin_cache[key]['diffs'])
for key in spin_cache:
    if spin_cache[key]['diffs']:
        # print(spin_cache[key]['diffs'])
        ans = spin_cache[key]['list'][-1]
        if ans%reps + 1 == 1000000000%reps:
            complete_answer =key
        c += 1

print(complete_answer)