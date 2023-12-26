def transpose(input):
    transposed = ['' for i in range(len(input[0]))]
    for line in input:
        for i, c in enumerate(line):
            transposed[i] += c
    return transposed

def expend(input):
    qty = 0
    spaced = input.copy()
    for i, line in enumerate(input):
        if not '#' in line:
            spaced.insert(i + qty, line)
            qty += 1
    return spaced

def calc_distance(star1, star2):
    return abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])

input_path = 'day11/input/input.txt'

file = open(input_path).read().strip()
old_galaxy = file.split('\n')

new_galaxy = expend(transpose(expend(old_galaxy)))

stars = []
for i, line in enumerate(new_galaxy):
    for j, c in enumerate(line):
        if c == '#':
            stars.append((i, j))

total = 0
for i in range(len(stars) -1):
    star1 = stars[i]
    for star2 in stars[i + 1:]:
        total += calc_distance(star1, star2)

print(total)