input_path = 'day6/input/example.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

time = []
digit = ''
for c in lines[0]:
    if c.isdigit():
        digit += c
        continue
    if not c.isdigit() and len(digit) != 0:
        time.append(int(digit))
        digit = ''
if len(digit) != 0:
    time.append(int(digit))

distance = []
digit = ''
for c in lines[1]:
    if c.isdigit():
        digit += c
        continue
    if not c.isdigit() and len(digit) != 0:
        distance.append(int(digit))
        digit = ''
if len(digit) != 0:
    distance.append(int(digit))


options_to_win = {}
for race in range(len(time)):
    options_to_win[race] = 0
    for ms in range(0, time[race] + 1, 1):
        if ms * (time[race]-ms) > distance[race]:
            options_to_win[race] += 1

tot_number = 1
for k, v in options_to_win.items():
    tot_number *= v

print(tot_number)