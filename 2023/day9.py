_input = open('input.txt').read().split('\n')

predictions = []
for line in _input:
	history = list(map(int, line.split()))
	differences = [history]
	prediction = 0
	while not all(diff == 0 for diff in differences[-1]):
		next_diff = []
		last_diff = differences[-1]
		for i in range(len(last_diff)-1):
			next_diff.append(last_diff[i+1] - last_diff[i])

		differences.append(next_diff)
	

	prediction = 0
	for diff in differences[::-1]:
		prediction = diff[0] - prediction


	predictions.append(prediction)
print(sum(predictions))