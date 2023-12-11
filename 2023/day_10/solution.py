grid = [list(x) for x in open('input.txt').read().split('\n')]

start = ()

def add(one, two):
    return tuple(map(lambda i, j: i + j, one, two))

def neg(a):
    return tuple(map(lambda i: -i, a))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i,j)

sign_dict1 = {
    '|': ['north', 'south'],
    '-': ['east', 'west'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south', 'east'],
    '.': []
}

sign_dict = {
    '|': [(-1,0), (1,0)],
    '-': [(0,1),  (0, -1)],
    'L': [(-1,0), (0,1)],
    'J': [(-1,0), (0,-1)],
    '7': [(1,0), (0,-1)],
    'F': [(1,0), (0,1)],
    '.': [],
    'S': []
}

def search(grid, start):
    i,j = start
    around = {}
    list_ = []
    for i1 in range(-1,2):
        for j1 in range(-1,2):
            if (-i1,-j1) in sign_dict[grid[i+i1][j+j1]]:
                list_.append([(i1,j1), grid[i+i1][j+j1]])
    return list_



list_ = search(grid, start)
start_connects = list_
origins = [start for x in list_]

inc = 0

locations = []

while True:

    loc = []
    for origin, sign in zip(origins, list_):
        a = add(origin, sign[0])
        loc.append(a)

    if len(set(loc)) == 1:
        locations.append(loc)
        inc += 1
        break

    found = []
    starts = []
    for origin,sign in zip(origins, list_):
        dirs = sign_dict[sign[1]]
        a = add(origin,sign[0])
        starts.append(a)
        b = neg(sign[0])
        ind = 1- dirs.index(b)
        c = add(a,dirs[ind])
        found.append([dirs[ind], grid[c[0]][c[1]]])
    origins = starts
    list_ = found
    locations.append(loc)
    inc += 1


def print_grid(grid):
    for i in range(len(grid)):
        print('')
        print(grid[i])
# n = next(origins, list_)
# print(len(n)/2)
print(inc)
locations.append([(start[0],start[1])])
i2 = start[0]
j2 = start[1]

direcs = [x[0] for x in start_connects]

for key in sign_dict:
    if direcs[0] in sign_dict[key] and direcs[1] in sign_dict[key]:
        grid[start[0]][start[1]] = key




for i in range(len(grid)):
    for j in range(len(grid[i])):
        is_there = False
        for loc in locations:
            if (i,j) in loc or grid[i][j] == 'S':
                is_there = True
        if not is_there:
            grid[i][j] = '0'

grid2  = []
print(1)

for i in range(len(grid)):
    lat = ['I'] * (len(grid[i])*2)
    below = ['I'] * len(lat)
    for j in range(len(grid[i])):
        for loc in locations:
            char = grid[i][j]
            if char in sign_dict:
                if (0,1) in sign_dict[char]:
                    lat[j*2+1] = '-'
                if (1,0) in sign_dict[char]:
                    below[j*2] = '|'
            lat[j*2] = char
    grid2.append(lat)
    grid2.append(below)

print(2)

# grid.insert(1, ['0']*len(grid[0]))

assert (len(grid2) == len(grid)*2)

areas = []


def initial_enclosed(grid, i,j):

    # for loc in locations:
    if grid[i][j] in sign_dict:
        return grid[i][j]

    if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[i])-1:
        return '0'
    return 'I'


for i in range(len(grid2)):
    for j in range(len(grid2[i])):
        grid2[i][j] = initial_enclosed(grid2, i,j)

# print_grid(grid2)
print(3)

def enclosed_2(grid, i,j):
    culprits = []

    if grid[i][j] == '0':
        for i1 in range(-1,2):
            for j1 in range(-1,2):
                i2 = i + i1
                j2 = j + j1
                if not ((i2 < 0 or i2 >= len(grid)) or (j2 < 0 or j2 >= len(grid[i]))):

                    neighbour = grid[i2][j2]
                    if neighbour == 'I':
                        
                        grid[i2][j2] = '0'
                        culprits.append((i2,j2))
    return culprits
        



    


for i in range(len(grid2)):
    for j in range(len(grid2[i])):

        culprits = [(i,j)]
        while culprits:
            new_c = []
            for cuplrit in culprits:
                new_c.extend(enclosed_2(grid2, cuplrit[0], cuplrit[1]))
            culprits = new_c
    


print(4)


for i in range(len(grid)):
    for j in range(len(grid[i])):

        grid[i][j] = grid2[i*2][j*2]







print(5)


counter = 0
                
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'I':
            counter += 1


print(counter)

