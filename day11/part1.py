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

input_path = 'day11/input/example.txt'

file = open(input_path).read().strip()
old_galaxy = file.split('\n')

new_galaxy = expend(transpose(expend(old_galaxy)))
