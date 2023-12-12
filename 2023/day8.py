from math import gcd

instructions, nodes = open('input.txt', 'r').read().split('\n\n')

def lcm(numbers):
	result = 1
	for number in numbers:
		result = result*number//gcd(result, number)
	return(result)

nodes_dict = {}
for node in nodes.split('\n'):

	label, direction = node.split(' = ')
	direction = direction.split(', ')

	nodes_dict[label] = (direction[0][1:], direction[1][:-1])

dests = []
for key in nodes_dict.keys():
	if key[-1] == 'A':
		dests.append(key)

counts = []
for dest in dests:
	counter = 1
	while not dest[-1] == 'Z':
		instruction = instructions[(counter%len(instructions)) -1]
		counter +=1
		if instruction == 'L':
			instruction = 0
		else:
			instruction = 1
		dest = nodes_dict[dest][instruction]
	print(counter)

	counts.append(counter-1)

print(lcm(counts))




# while not all(dest[-1] == 'Z' for dest in dests):
# 	instruction = instructions[(counter%len(instructions)) -1]
# 	if instruction == 'L':
# 		instruction = 0
# 	else:
# 		instruction = 1
# 	dests = [nodes_dict[dest][instruction] for dest in dests]
# 	counter += 1
# 	print(dests)
	
# 	if dests in previous_dests:
# 		exit()
# 	previous_dests.append(dests)
# print(counter-1)



