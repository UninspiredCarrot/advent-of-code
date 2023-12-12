file1 = open('input.txt', 'r')
lines = file1.readlines()

nums = '0123456789'

schematic = []
for i in range(len(lines)):
	schematic.append([])
	for j in range(len(lines[i])):
		schematic[i].append(lines[i][j])

num_list = []
pt_list = []
gr_list = []

for i in range(len(schematic)):
	number = ''
	pts = []
	for j in range(len(schematic[i])):
		
		if schematic[i][j] in nums:
			number+=(schematic[i][j])
			pts.append((i,j))
		else:
			if schematic[i][j] == '*':
				gr_list.append((i,j))
			if number != '':
				num_list.append(int(number))
				number = ''
				pt_list.append(pts)
				pts = []

border_list = []

for pts in pt_list:
	temp_border = set()
	border = set()
	bin = [-1,0,1]
	incs = [[x,y] for x in bin for y in bin]
	for pt in pts:
		for inc in incs:
			temp_border.add((pt[0]+inc[0], pt[1]+inc[1]))
		for x in temp_border:
			# print(list(x))
			# print(pts)
			if x[0] >= 0 and x[1] >= 0 and x[0] < len(schematic) and x[1] < len(schematic[0]) and x not in pts:
				border.add(x)
	border_list.append(border)

sum = 0
valid_list = []
for i in range(len(num_list)):
	valid = False
	# print(num_list[i])
	for border in border_list[i]:

		# print(schematic[border[0]][border[1]])
		if schematic[border[0]][border[1]] not in '123456789.\n':
			valid = True

	valid_list.append(valid)
	if valid:
		sum+=num_list[i]


#for i in range(len(num_list)):
	# print(f'{num_list[i]}: {border_list[i]} -> {pt_list[i]}')
	#print(f'{num_list[i]}: {[schematic[x[0]][x[1]] for x in border_list[i]]} -> {valid_list[i]}')
print(sum)

ratio = 0
for gr in gr_list:
	num_gr = set()
	for i in range(len(num_list)):
		if gr in border_list[i]:
			num_gr.add(num_list[i])
	if len(num_gr) == 2:
		ratio+=list(num_gr)[0]*list(num_gr)[1]
print(ratio)


