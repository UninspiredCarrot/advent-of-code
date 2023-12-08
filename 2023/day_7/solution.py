from functools import cmp_to_key

file = open('input.txt').read()

lines = file.split('\n')

deck = [tuple(line.split()) for line in lines]


label_hierarchy = list('AKQT98765432J')

type_hierarchy = "high one two three full four five".split()

def compare(hand_1, hand_2):
	if hand_1[0] != hand_2[0]:
		return hand_2[0]-hand_1[0] 


	hand_1 = list(hand_1[1])
	hand_2 = list(hand_2[1])



	index = 0
	while index < 5:
		if label_hierarchy.index(hand_1[index]) > label_hierarchy.index(hand_2[index]):
			return -1
		if label_hierarchy.index(hand_1[index]) < label_hierarchy.index(hand_2[index]):
			return 1
		index+=1
	return 0

def typer(cards):
	cards = list(cards)
	

	no_jokers = cards.count('J')
	

	cards = [x for x in cards if x != 'J']

	card_set = set(cards)



	no_duplicates = sorted([[cards.count(x), x] for x in card_set])[::-1]


	if len(no_duplicates) == 0:
		no_duplicates.append([no_jokers, 'J'])
	else:

		no_duplicates[0][0] = no_duplicates[0][0] + no_jokers
	print(cards)
	print(no_duplicates)

	


	
	if no_duplicates[0][0] == 5:
		return 1
	if no_duplicates[0][0] == 4:
		return 2
	if no_duplicates[0][0] == 3:
		if no_duplicates[1][0] == 2:
			return 3
		return 4
	if no_duplicates[0][0] == 2:
		if no_duplicates[1][0] == 2:
			return 5
		return 6
	return 7

hands = []
for cards, bid in deck:
	hands.append((typer(cards), cards, bid))


hands = sorted(hands,key=cmp_to_key(compare))


total = 0
rank = 1

for hand in hands:
	total += rank*int(hand[-1])
	rank+=1


print(hands)
print(total)