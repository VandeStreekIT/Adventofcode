# start with
counter = 0

input_path = 'day1/input/input.txt'

with open(input_path) as input:
    for line in input:

        # get first digit from line
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        # get last digit from line
        for char in line[::-1]:
            if char.isdigit():
                last_digit = char
                break
        
        # concat digits to int
        cal_value = int(first_digit + last_digit)

        counter = counter + cal_value

print(counter)