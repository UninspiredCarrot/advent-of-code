file = open('input.txt', 'r').read()

times, rec_distances = file.split('\n')

time = int(''.join(times.split(':')[1].strip().split()))
rec_distance = int(''.join(rec_distances.split(':')[1].strip().split()))




ways_to_win = 0

for charge_time in range(time+1):
	
	speed = charge_time*1

	time_left = time - charge_time

	distance = time_left*speed

	if distance > rec_distance:
		ways_to_win += 1




print(ways_to_win)