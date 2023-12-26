input_path = 'day8/input/input.txt'

file = open(input_path).read()
instructions = file.split('\n\n')[0]
directions = file.split('\n\n')[1].split('\n')

locations = {}

for line in directions:
    location = line.split(' = ')[0]
    destinations = line.split(' = ')[1].strip('()').split(', ')
    locations[location] = {'L': destinations[0], 'R': destinations[1]}

start_locations = []
for location, destination in locations.items():
    if location.endswith('A'):
        start_locations.append(location)

phases = []
for s in start_locations:
    steps = 0
    finish_found = False

    next_location = s
    while not finish_found:
        for c in instructions:  
            steps += 1
            next_location = locations[next_location][c]
            if next_location.endswith('Z'):
                finish_found = True
                break
    phases.append(int(steps/len(instructions)))

total_steps = 1
for phase in phases:
    total_steps *= phase

print(total_steps * len(instructions))
