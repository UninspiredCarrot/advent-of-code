image = [list(x) for x in open('input.txt').read().split('\n')]

def print_image(image):
    
    for i in range(len(image)):
        print(image[i])


times = 1000000
#expand
def expand_rows(image):
    list_ = []
    for i in range(len(image)):
        empty_row = ['.']*len(image[i])
        if image[i] == empty_row:
            list_.append(i)

    return list_

def expand_columns(image):
    empty_columns = []
    empty_row_no = [True]*len(image[0])
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == '#':
                empty_row_no[j] = False
    
    for i in range(len(empty_row_no)):
        if empty_row_no[i]:
            empty_columns.append(i)

    return empty_columns



empty_rows = expand_rows(image)
empty_columns = expand_columns(image)

print(empty_columns, empty_rows)


#label and pair


def label(image):
    galaxies = {}
    counter = 1
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == '#':
                galaxies[counter] = (i,j)
                counter+=1

    return galaxies

galaxies = label(image)


def generate_pairs(highest):
    pairs = []
    for i in range(1, highest+1):
        for j in range(i+1, highest+1):
            pairs.append((i,j))
    return pairs

pairs = generate_pairs(list(galaxies.keys())[-1])


def shortest_path(pair):
    a = galaxies[pair[0]]
    b = galaxies[pair[1]]

    longs = sorted([b[0], a[0]])
    lats = sorted([b[1], a[1]])


    longitude = longs[1] - longs[0]
    latitude = lats[1] - lats[0]

    count = 0
    for row in empty_rows:
        if row in range(longs[0],longs[1]):
            count += 1
    
    longitude += count*(times-1)

    count = 0
    for column in empty_columns:
        if column in range(lats[0],lats[1]):
            count+=1

    latitude += count*(times-1)
    return longitude+latitude




# print(shortest_path((5,9)))

sum = 0
for pair in pairs:
    sum += shortest_path(pair)
print(sum)


