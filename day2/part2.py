sum = 0

file = open('day2/input/input.txt')
lines = file.read().splitlines()

for line in lines:
    min = {'red': 0, 'green': 0, 'blue': 0}

    game = line.split(':')[0].split(' ')[1]
    graps = line.split(':')[1].split(';')
    for grap in graps:
        groups = grap.strip().split(',')
        for group in groups:
            color = group.strip().split(' ')[1]
            qty = int(group.strip().split(' ')[0])
            if (min[color] == 0) or (min[color] < qty):
                min[color] = qty
    power = min['red'] * min['green'] * min['blue']
    sum = sum + power

print(sum)
file.close()