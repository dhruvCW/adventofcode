
from typing import List


def parse_from_file(filename: str) -> List[List[int]]:
    result = []
    with open(filename) as file:
        for line in file:
            result.append([int(item) for item in line.split()])
        
    return result