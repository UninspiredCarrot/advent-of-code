file1 = open('input.txt', 'r')
lines = file1.readlines()
sum = 0
for line in lines:
	
	line = line.split(":")
	id = int(line[0].split(" ")[1])
	sets = line[1].split(";")
	max_red = 0
	max_green = 0
	max_blue = 0
	for set in sets:
		red_count = 0
		green_count = 0
		blue_count = 0
		colours = set.split(",")
		for colour in colours:
			number = int(colour.strip().split(" ")[0])
			if "blue" in colour:
				blue_count+=number
			if "red" in colour:
				red_count+=number
			if "green" in colour:
				green_count+=number
		if red_count>=max_red:
			max_red = red_count
		if blue_count>=max_blue:
			max_blue = blue_count
		if green_count>=max_green:
			max_green = green_count
	print(f'red: {max_red}, green: {max_green}, blue: {max_blue}')
	power = max_red*max_blue*max_green
	sum += power
print(sum)