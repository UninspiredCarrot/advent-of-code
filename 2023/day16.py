import time











def do(start_x,start_y, prev_x, prev_y):


    grid = [list(x) for x in open('input.txt').read().split('\n')]
    def check(cache, last_point,x,y, grid):
        if (last_point,x,y) in cache:

            return False
        
        if y >= len(grid) or y < 0 or x >= len(grid[0]) or x < 0:
            return False

        cache.add((last_point,x,y))
        return True
    
    def view(cache, grid):

        new = grid
        for _,i,j in cache:
            new[j][i] = '#'


        return new
    
    cache = set()
    
    x = start_x
    y = start_y
    cache.add((None, x, y))
    last_x = prev_x
    last_y = prev_y
    pointers = [[(last_y,last_x),(y,x)]]

    while True:
        lens = [len(x) for x in pointers]
        for pointer in pointers:
            point = pointer[-1]
            last_point = pointer[-2]


            x = point[1]
            y = point[0]

            now = grid[y][x]

            last_x = last_point[1]
            last_y = last_point[0]

            delta_x = x - last_x
            delta_y = y - last_y

            #print(f'x: {x}, y: {y}, last x: {last_x}, last y: {last_y}, delta x: {delta_x}, delta y: {delta_y}')

            new_x = x
            new_y = y

            if now == '.':
                new_x = delta_x + x
                new_y = delta_y + y

            if now == '/':
                if delta_x != 0:
                    new_y = -delta_x + y
                if delta_y != 0:
                    new_x = -delta_y + x

            if now == '\\':
                if delta_x != 0:
                    new_y = delta_x + y
                    new_y = delta_x + y
                if delta_y != 0:
                    new_x = delta_y + x
                    new_y = y

            if (now == '|' and delta_x != 0) or (now == '-' and delta_y != 0):
                y1 = -delta_x + y
                x1 = -delta_y + x
                if check(cache,(x,y),x1,y1,grid):
                    pointers.append([(y,x),(y1,x1)])
                new_y = delta_x + y
                new_x = delta_y + x
                
                

            if (now == '|' and delta_y != 0) or (now == '-' and delta_x != 0):
                new_x = delta_x + x
                new_y = delta_y + y

            if check(cache,(x,y),new_x,new_y,grid):
                pointer.append((new_y, new_x))


        new_lens = [len(x) for x in pointers]
        if lens == new_lens:
            break

    new = view(cache,grid)

    count = 0
    for line in new:
        # print(line)
        for i in line:
            if i == '#':
                count += 1


    return count


inp = [list(x) for x in open('input.txt').read().split('\n')]
xs = [i for i in range(len(inp))]
ys = [i for i in range(len(inp[0]))]

list_ = [(0,1),(0,-1),(1,0),(-1,0)]

counts = []
for i in range(2):

    put = [0,0,0,0]
    put[2+i] = -1
    
    put[i] = 0
    if i == 0:
        use = ys
    else:
        use = xs
    for j in range(len(use)):
        put[1-i] = use[j]
        put[3-i] = use[j]


        counts.append(do(put[0],put[1],put[2],put[3]))
        put[1-i] = 0
        put[3-i] = 0
    
    put[2+i] = xs[-1]+1
    if i == 0:
        put[i] = xs[-1]
        use = ys
    else:
        put[i] = xs[-1]
        use = xs
    for j in range(len(use)):
        put[1-i] = use[j]
        put[3-i] = use[j]



        counts.append(do(put[0],put[1],put[2],put[3]))
        put[1-i] = 0
        put[3-i] = 0

    




print(max(counts))
