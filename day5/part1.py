from operator import itemgetter

input_path = 'day5/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))
categories = ['seed-to-soil', 
              'soil-to-fertilizer',
              'fertilizer-to-water',
              'water-to-light map:',
              'light-to-temperature map:',
              'temperature-to-humidity map:',
              'humidity-to-location map:']

def get_mapping(lines):
    mapping = {}
    for category in categories:
        mapping[category] = []
        for i, line in enumerate(lines):
            if len(mapping[category]) != 0:
                break
            if line.startswith(category):
                for j, values in enumerate(lines[i+1:]):
                    if values == '':
                        break
                    mapping[category].append(list(map(int, values.split(' '))))
            mapping[category] = sorted(mapping[category], key= itemgetter(1),reverse= True)
            continue
    return mapping

def get_mapping_values(category, index, mapping):

    for values in mapping[category]:
        if index < values[1]:
            continue
        if index > (values[1] + values[2]):
            break
        index = values[0] + (index - values[1])
        break

    return index

def get_location_from_seed(seed, mapping):
    index = seed
    for category in categories:
        index = get_mapping_values(category, index, mapping)
    return index

mapping = get_mapping(lines)

locations = []
for seed in seeds:
    locations.append(get_location_from_seed(seed, mapping))

print(min(locations))