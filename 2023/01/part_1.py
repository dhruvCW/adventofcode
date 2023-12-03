from typing import TextIO

def calibration_value(line: str) -> int:
    digits = [int(s) for s in line if s.isdigit()]
    return (digits[0] * 10 + digits[-1])

def sum_all_calibration_values(file: TextIO) -> int:
    sum = 0
    while line := file.readline():
        sum += calibration_value(line)

    return sum

with open('input.txt') as file:
    print(f"sum is {sum_all_calibration_values(file)}")