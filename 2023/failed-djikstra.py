import heapq
import numpy as np


np.set_printoptions( linewidth=500)
block = [list(map(int, x)) for x in open('input.txt').read().split('\n')]

print(block)


block = np.array(block)





def check(x, y, grid):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    return True

start = (0,0)
def dijkstra(block, shape, start, end):

    heats = np.full(shape, np.inf)
    heats[start[1]][start[0]] = 0
    priority_q = []
    previous = np.full(shape, None)
    heapq.heappush(priority_q, (0, start, (0,0), 0))
    neighbours = []

    while priority_q:
        print(f'new: {[(x[0], x[1], x[2], x[-1]) for x in neighbours]}')
        heat, point, past, streak = heapq.heappop(priority_q)
        
        print(heat, point, past, streak)
        # print(point, end)
        if point == end:
            print(heats)
            return heat,previous
        # print(past)
        past_pt = past
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        new_past = point
        neighbours = []
        for direction in directions:

            new_point = (point[0]+direction[0], point[1]+direction[1])



            if check(new_point[0], new_point[1], block):

                if direction == (point[0]-past_pt[0], point[1]-past_pt[1]):
                    new_streak = streak + 1
                else:
                    new_streak = 1

                new_heat = heat + block[new_point[1]][new_point[0]]
                
                

                if new_streak <= 3 and new_point != past_pt and new_heat <= heats[new_point[1]][new_point[0]]:
                    
                    if new_heat == heats[new_point[1]][new_point[0]]:
                        if [x for x in priority_q if x[1] == new_point] != []:

                            if new_streak < priority_q[priority_q.index([x for x in priority_q if x[1] == new_point][0])][-1]:
                                priority_q.remove([x for x in priority_q if x[1] == new_point][0])
                                neighbours.append((new_heat, new_point, new_past, new_streak))
                                heapq.heappush(priority_q, (new_heat, new_point, new_past, new_streak))

                        else:
                            continue
                    if new_heat < heats[new_point[1]][new_point[0]]:
                        heats[new_point[1]][new_point[0]] = new_heat
                        previous[new_point[1]][new_point[0]] = new_past
                        neighbours.append((new_heat, new_point, new_past, new_streak))


                        heapq.heappush(priority_q, (new_heat, new_point, new_past, new_streak))

        if len(neighbours) == 0:
            heats[point[1]][point[0]] = np.inf
                    

                



end = (len(block[0]),len(block)-1)


heat,past = dijkstra(block, np.shape(block), start, end)

print(heat)

print(past)

# dirs = {
#     10: '>',
#     1: '!',
#     -1: '^',
#     -10: '<'

# }


# def show(previous, block, end):
#     new_block = block.astype(object)
#     from_ = end
#     to = previous[from_[1]][from_[0]]
#     total = []
#     while to != None:
#         total.append(block[from_[1]][from_[0]])
#         dir = (from_[0] - to[0], from_[1] - to[1])
#         sign = dirs[10*dir[0]+ 1*dir[1]]
#         # print(from_, to, sign)
#         new_block[from_[1]][from_[0]] = sign

#         from_ = to
#         to = previous[from_[1]][from_[0]]
#         # time.sleep(1)

#     return sum(total), new_block

# total, new_block = show(previous, block, end)
# print(new_block)
# print(distances)
# print(total)

# # print(distances)