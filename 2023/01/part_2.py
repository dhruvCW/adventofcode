from typing import TextIO

def convert_digit(digit: str) -> int:
    if digit.isdigit():
        return int(digit)
    
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for index, number in enumerate(numbers):
        if digit == number:
            return index + 1

    raise ValueError(f"invalid number {digit}")

def calibration_value(line: str) -> int:
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    index_map = {}
    for number in numbers:
        try:
            index_map[line.index(number)] = number
            index_map[line.rindex(number)] = number
        except ValueError:
            pass

    start_digit = convert_digit(index_map[min(index_map.keys())])
    end_digit = convert_digit(index_map[max(index_map.keys())])
    
    return (start_digit * 10 + end_digit)

def sum_all_calibration_values(file: TextIO) -> int:
    sum = 0
    while line := file.readline():
        value = calibration_value(line.strip())
        sum += value

    return sum

with open('input.txt') as file:
    print(f"sum is {sum_all_calibration_values(file)}")