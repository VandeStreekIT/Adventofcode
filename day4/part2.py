input_path = 'day4/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

sum = 0
number_of_games = len(lines)
cards = number_of_games * [1]

for i, line in enumerate(lines):
    winningnumbers = line.split('|')[0].strip().split(':')[1].strip().split(' ')
    numbers_you_have = line.split('|')[1].strip().replace('  ',' ').split(' ')

    count_matching = 0
    for number in numbers_you_have:
        if number in winningnumbers:
            count_matching += 1

    for k in range(count_matching):
        if i + k < len(cards):
            cards[i+k+1] += cards[i]

for card in cards:
    sum += card

print(sum)