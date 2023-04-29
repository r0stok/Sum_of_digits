def sum_of_digits(num):

    assert 1 <= len(str(num)) <= 10, "Input number must have between 1 and 10 digits"
    assert num >= 0, "Input number must be positive"

    return sum(int(digit) for digit in str(num))

import csv

with open('test_numbers.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        num = int(row[0])
        digit_sum = sum_of_digits(num)
        print(f"Number: {num}, Digit Sum: {digit_sum}")