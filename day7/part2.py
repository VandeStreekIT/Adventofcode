def get_hand_value(hand, joker):
    structure = []
    most_common_card = ''
    counter = 0
    if not (hand == 5 * joker):
        for value in list(set(hand)):
            if value == joker:
                continue
            if hand.count(value) > counter:
                counter = hand.count(value)
                most_common_card = value
        hand = hand.replace(joker, most_common_card)

    for value in list(set(hand)):
        structure.append(hand.count(value))
    return tuple(sorted(structure, reverse=True))

input_path = 'day7/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

card_order = {'A': 0, 'K': 1, 'Q': 2, 'J': 13, 'T': 4, '9': 5, '8': 6, 
         '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

hand_value_order = {
    (1, 1, 1, 1, 1): 0,
    (2, 1, 1, 1): 1,
    (2, 2, 1): 2,
    (3, 1, 1): 3,
    (3, 2): 4,
    (4, 1): 5,
    (5,): 6
}

results = {}
for hand_value, order in hand_value_order.items():
    results[hand_value] = {}

games = {}
for line in lines:
    h = line.split()[0]
    b = int(line.split()[1])
    games[h] = b

for hand, bet in games.items():
    


    results[get_hand_value(hand, 'J')][hand] = bet

score = 0
rank = 0

for i, hands in results.items():
    sorted_hands = sorted(hands, key=lambda d: [card_order[v] for v in d], reverse=True)
    for hand in sorted_hands:
        rank += 1
        score += rank * games[hand]

print(score)