from operator import itemgetter

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
            mapping[category] = sorted(mapping[category], key= itemgetter(1))
            continue
    return mapping

def knip_range_obv_mapping_per_range(range, mapping, category):
    new_range = {}
    for k, v in range.items():
        rstart = k
        rend = k + v
        rest = True

        for map in mapping[category]:
            mgoal = map[0]
            mstart = map[1]
            msize = map[2]
            mend = mstart + msize

            if mend <= rstart: continue
            
            if mstart >= rend: continue

            if (mstart <= rstart) and (mend >= rend):
                new_range[rstart + (mgoal - mstart)] = rend - rstart
                rest = False
                continue

            if (mstart <= rstart) and (mend >= rstart) and (mend <= rend):
                new_range[rstart + (mgoal - mstart)] = mend - rstart
                rstart = mend
                continue

            if (mstart >= rstart) and (mend <= rend):
                new_range[rstart] = mstart - rstart
                new_range[mstart + (mgoal - mstart)] = mend - mstart
                rstart = mend
                continue

            if (mstart >= rstart) and (mstart <= rend) and (mend >= rend):
                new_range[rstart] = mstart - rstart
                new_range[mstart + (mgoal - mstart)] = rend - mstart
                rest = False
                continue

        if rest and not (mend == rend):
            new_range[rstart] = rend - rstart
    
    return dict(sorted(new_range.items()))


# program
input_path = 'day5/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

seeds_line = list(map(int, lines[0].split(':')[1].strip().split(' ')))
seed_ranges = {}

for i in range(0, len(seeds_line) ,2):
    seed_ranges[seeds_line[i]] = seeds_line[i+1]

seed_ranges = dict(sorted(seed_ranges.items()))

categories = ['seed-to-soil', 
              'soil-to-fertilizer',
              'fertilizer-to-water',
              'water-to-light map:',
              'light-to-temperature map:',
              'temperature-to-humidity map:',
              'humidity-to-location map:']

mapping = get_mapping(lines)

range = seed_ranges
for category in categories:
    range = knip_range_obv_mapping_per_range(range, mapping, category)

print(list(range.keys())[0])