def extrapolate_b(list):
    if all([v == list[0] for v in list]):
        return list[0]
    new_list = []
    for i in range(len(list) -1):
        new_list.append(list[i+1] - list[i])
    return list[0] - extrapolate_b(new_list)

input_path = 'day9/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

score = 0

for line in lines:
    sequence = [int(i) for i in line.split()]
    score += extrapolate_b(sequence)

print(score)
