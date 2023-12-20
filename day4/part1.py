input_path = 'day4/input/input.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

sum = 0

for line in lines:
    winningnumbers = line.split('|')[0].strip().split(':')[1].strip().split(' ')
    numbers_you_have = line.split('|')[1].strip().replace('  ',' ').split(' ')

    count_matching = 0
    for number in numbers_you_have:
        if number in winningnumbers:
            count_matching += 1

    if count_matching != 0:
        sum = sum + 2**(count_matching -1)

print(sum)