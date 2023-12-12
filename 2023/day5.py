file = open('input.txt', 'r')
lines = file.read()


inputs, *almanac = lines.split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
	seeds.append((inputs[i], inputs[i + 1] + inputs[i]))



for maps in almanac:

	_map = []
	for line in maps.splitlines()[1:]:
		_map.append(list(map(int, line.split())))
	locations = []
	while len(seeds) > 0:
		seed_start, seed_end = seeds.pop()

		for dest, source, _range in _map:
			overlap_start = max(seed_start, source)
			overlap_end = min(seed_end, source+_range)

			if overlap_start < overlap_end:
				locations.append((overlap_start - source + dest, overlap_end- source + dest))
				if overlap_start > seed_start:
					seeds.append((seed_start, overlap_start))
				if overlap_end < seed_end:
					seeds.append((overlap_end, seed_end))
				break
		else:
			locations.append((seed_start, seed_end))	

	seeds = locations
print(min(locations)[0])
