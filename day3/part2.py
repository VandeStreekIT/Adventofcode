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
        if c != '*':
            continue
        
        # determine if there are exactly two values
        count = 0
        list_of_values = []

        for k in range(i-1, i+2):
            check_string = lines[k][j-1:j+2]
            if len(check_string.strip('.*')) == 0:
                continue
            elif len(check_string.strip('.*')) == 1:
                
                # determine value
                value = ''
                if check_string[0].isdigit():
                    index = j-1
                    while lines[k][index-1].isdigit():
                        index -= 1
                elif check_string[1].isdigit():
                    index = j
                else:
                    index = j+1
                
                while lines[k][index].isdigit():
                    value = value + lines[k][index]
                    index += 1
                
                list_of_values.append(int(value))
                
            else:
                if check_string[1].isdigit():

                    # determine value
                    value = ''
                    if check_string[0].isdigit():
                        index = j-1
                        while lines[k][index-1].isdigit():
                            index -= 1
                    elif check_string[1].isdigit():
                        index = j
                    else:
                        index = j+1
                    
                    while lines[k][index].isdigit():
                        value = value + lines[k][index]
                        index += 1
                    
                    list_of_values.append(int(value))

                else:
                    # determine value
                    for index in [j-1, j+1]:
                        value = ''
                        while lines[k][index-1].isdigit():
                            index -= 1
                        while lines[k][index].isdigit():
                            value = value + lines[k][index]
                            index += 1

                        list_of_values.append(int(value))

        if len(list_of_values) == 2:
            sum = sum + (list_of_values[0] * list_of_values[1])

print(sum)
            
