sum = 0

file = open('day2/input/input.txt')
lines = file.read().splitlines()

for line in lines:
    max = {'red': 0, 'green': 0, 'blue': 0}

    game = line.split(':')[0].split(' ')[1]
    graps = line.split(':')[1].split(';')
    for grap in graps:
        groups = grap.strip().split(',')
        for group in groups:
            color = group.strip().split(' ')[1]
            qty = int(group.strip().split(' ')[0])
            if max[color] < qty:
                max[color] = qty
    if (max['red'] > 12) or (max['green'] > 13) or (max['blue'] > 14):
        continue
    sum = sum + int(game)

print(sum)