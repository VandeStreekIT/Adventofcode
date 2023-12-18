import re

# start with default parameters
counter = 0

input_path = 'day1/input/input.txt'

spelled_out = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open(input_path) as input:
    for line in input:

        first_index = -1
        last_index = -1

        first_spelled_digit = ''
        last_spelled_digit = ''

        # find first and last spelled digit
        for k, v in spelled_out.items():
            index =[m.start() for m in re.finditer(k, line)]

            if len(index) == 0:
                continue

            if (first_index == -1) or (first_index > index[0]):
                first_index = index[0]
                first_spelled_digit = k

            if (last_index < index[-1]):
                last_index = index[-1]
                last_spelled_digit = k


        # replace first and last spelled digit
        line_first_digit = line

        if first_index != -1:
            line_first_digit = (
                line[0:first_index] 
                + spelled_out[first_spelled_digit] 
                + line[first_index + len(first_spelled_digit): -1])
        
        
        line_last_digit = line

        if last_index != -1:
            line_last_digit = (
                line[0:last_index] 
                + spelled_out[last_spelled_digit] 
                + line[last_index + len(last_spelled_digit): -1])    


        # get first digit from line
        for char in line_first_digit:
            if char.isdigit():
                first_digit = char
                break

        # get last digit from line
        for char in line_last_digit[::-1]:
            if char.isdigit():
                last_digit = char
                break
        
        # concat digits to int
        cal_value = int(first_digit + last_digit)

        counter = counter + cal_value

print(counter)