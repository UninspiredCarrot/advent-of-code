from heapq import heappush, heappop

grid = [list(map(int, line.strip())) for line in open('input.txt')]

seen = set()

def check(x, y, grid):
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return False
    return True

priority_q = [(0, 0, 0, 0, 0, 0)]

while priority_q:
    heat_loss, x, y, dx, dy, streak = heappop(priority_q)

    if x == len(grid[0]) - 1 and y == len(grid) - 1:
        print(heat_loss)
        break

    if (x, y, dx, dy, streak) in seen:
        continue

    seen.add((x, y, dx, dy, streak))

    if streak < 3 and (dx, dy) != (0,0):
        new_x = x + dx
        new_y = y + dy

        if check(new_x, new_y, grid):
            heappush(priority_q, (heat_loss + grid[new_y][new_x], new_x, new_y, dx, dy, streak + 1))


    for new_dx, new_dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if (new_dx, new_dy) != (dx, dy) and (new_dx, new_dy) != (-dx, -dy):
            new_x = x + new_dx
            new_y = y + new_dy

            if check(new_x, new_y, grid):
                heappush(priority_q, (heat_loss + grid[new_y][new_x], new_x, new_y, new_dx, new_dy, 1))

