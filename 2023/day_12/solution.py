from functools import cache
# cache = {}
@cache
def count(cfg, group_sizes):
    # Base case: if the configuration is empty
    if not cfg:
        # Return 1 if there are no remaining group sizes, 0 otherwise
        if not group_sizes:
            return 1
        else:
            return 0

    # Base case: if there are no remaining group sizes and no '#' in the configuration
    if not group_sizes and '#' not in cfg:
        # Return 1 because the configuration satisfies the conditions
        return 1
    
    # if (cfg,group_sizes) in cache:
    #     return cache[(cfg,group_sizes)]

    total_arrangements = 0

    # If the first character of the configuration is '.', it's an operational spring
    if cfg[0] in ".?":
        # Recursively call count_arrangements with the remaining configuration and the same group sizes
        total_arrangements += count(cfg[1:], group_sizes)

    # If the first character of the configuration is '#' or '?', it's a broken spring
    if cfg[0] in "#?":
        # Check if it's possible to place a contiguous group of size group_sizes[0] at the beginning of the configuration
        if group_sizes and group_sizes[0] <= len(cfg) and '.' not in cfg[:group_sizes[0]] and (group_sizes[0] == len(cfg) or cfg[group_sizes[0]] != "#"):
            # Recursively call count_arrangements with the remaining configuration and the remaining group sizes
            total_arrangements += count(cfg[group_sizes[0] + 1:], group_sizes[1:])


    # cache[(cfg,group_sizes)] = total_arrangements
    return total_arrangements

total = 0

for line in open('input.txt'):
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    
    cfg = "?".join([cfg] * 5)
    nums *= 5
    
    total += count(cfg, nums)

# Print the total number of arrangements
print(total)
