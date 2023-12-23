input_path = 'day7/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

order = {'A': 0, 
         'K': 1, 
         'Q': 2, 
         'J': 3, 
         'T': 4, 
         '9': 5, 
         '8': 6, 
         '7': 7, 
         '6': 8, 
         '5': 9, 
         '4': 10, 
         '3': 11, 
         '2': 12}

games = {}
for line in lines:
    h = line.split()[0]
    v = int(line.split()[1])
    games[h] = v

five_oak = {}
four_oak = {}
full_house = {}
three_oak = {}
two_pair = {}
one_pair = {}
high_card = {}

for hand, value in games.items():
    unique_values = list(set(hand))

    if len(unique_values) == 1:
        five_oak[hand] = value
        continue

    if len(unique_values) == 5:
        high_card[hand] = value
        continue

    if len(unique_values) == 2:
        if (hand.count(unique_values[1]) == 1 or
            hand.count(unique_values[1]) == 4):
            four_oak[hand] = value
        else:
            full_house[hand] = value
        continue

    if len(unique_values) == 4:
        one_pair[hand] = value
        continue

    if len(unique_values) == 3:
        if (hand.count(unique_values[0]) == 3 or
            hand.count(unique_values[1]) == 3 or 
            hand.count(unique_values[2]) == 3):
            three_oak[hand] = value
        else:
            two_pair[hand] = value
        continue


score = 0
rank = 0

for hand in sorted(high_card, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]
for hand in sorted(one_pair, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]
for hand in sorted(two_pair, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]
for hand in sorted(three_oak, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]
for hand in sorted(full_house, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]
for hand in sorted(four_oak, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]
for hand in sorted(five_oak, key=lambda d: [order[v] for v in d], reverse=True):
    rank += 1
    score += rank * games[hand]

print(score)