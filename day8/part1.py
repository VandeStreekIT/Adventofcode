input_path = 'day8/input/input.txt'

file = open(input_path).read()
instructions = file.split('\n\n')[0]
directions = file.split('\n\n')[1].split('\n')

locations = {}

for line in directions:
    location = line.split(' = ')[0]
    destinations = line.split(' = ')[1].strip('()').split(', ')
    locations[location] = {'L': destinations[0], 'R': destinations[1]}

start = 'AAA'
finish = 'ZZZ'
steps = 0
finish_found = False

next_location = start
while not finish_found:
    for c in instructions:  
        steps += 1
        next_location = locations[next_location][c]
        if next_location == finish:
            finish_found = True
            break
        
print(steps)