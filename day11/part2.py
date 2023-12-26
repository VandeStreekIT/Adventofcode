def transpose(input):
    transposed = ['' for i in range(len(input[0]))]
    for line in input:
        for i, c in enumerate(line):
            transposed[i] += c
    return transposed

def find_empty_lines(input):
    empty_lines = []
    for i, line in enumerate(input):
        if not '#' in line:
            empty_lines.append(i)
    return empty_lines

def calc_distance(star1, star2):
    multiplier = 999999
    count = 0
    

    rows_between = []
    rows_between = range(min(star1[0], star2[0]) + 1, 
                         max(star1[0], star2[0]))
    columns_between = range(min(star1[1], star2[1]) + 1, 
                         max(star1[1], star2[1]))
    
    count += len(list(set(rows_between) & set(empty_rows)))
    count += len(list(set(columns_between) & set(empty_columns)))

    return (abs(star1[0] - star2[0]) + 
            abs(star1[1] - star2[1]) + 
            (count * multiplier)
    )

input_path = 'day11/input/input.txt'

file = open(input_path).read().strip()
old_galaxy = file.split('\n')
trans_galaxy = transpose(old_galaxy)

empty_rows = find_empty_lines(old_galaxy)
empty_columns = find_empty_lines(trans_galaxy)

stars = []
for i, line in enumerate(old_galaxy):
    for j, c in enumerate(line):
        if c == '#':
            stars.append((i, j))

total = 0
for i in range(len(stars) -1):
    star1 = stars[i]
    for star2 in stars[i + 1:]:
        total += calc_distance(star1, star2)

print(total)