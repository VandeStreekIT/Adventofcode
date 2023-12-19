input_path = 'day3/input/example.txt'

file = open(input_path).read().strip()
lines = file.split('\n')

sum = 0
digit = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c.isdigit():
            digit.append(c)



            # if last digit of line

        else:
        
            #determine if symbol is near
        
            #reset digit
            digit = []




print(lines)
