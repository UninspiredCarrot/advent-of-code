file1 = open('input.txt', 'r')
lines = file1.readlines()

instances = [1]*len(lines)
copies = 0

count = 0

for line in lines:
	for instance in range(instances[count]):
		temp1 = line.split(":")
		temp2 = temp1[1].strip().split("|")
		winning_numbers = temp2[0].strip().split()
		my_numbers = temp2[1].strip().split()
		matches = []
		for mn in my_numbers:
			for wn in winning_numbers:
				if mn == wn:
					matches.append(mn)
		
		cnt = count + 1
		for match in matches:
			instances[cnt] += 1
			cnt += 1

	count += 1
	print(count)

print(sum(instances))