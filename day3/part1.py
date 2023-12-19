input_path = 'day3/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

lines.insert(0, '.' * len(lines[0]))
lines.append('.' * len(lines[0]))
lines = ['.' + line + '.' for line in lines]

sum = 0
digit = ''

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c.isdigit():
            digit = digit + c
            continue

        if len(digit) == 0:
            continue

        for k in range(i-1, i+2):
            check_string = lines[k][j - (len(digit)+1):j+1]
            if len(check_string.strip('.1234567890')) != 0:
                sum += int(digit)
                break
        
        digit = ''

print(sum)
