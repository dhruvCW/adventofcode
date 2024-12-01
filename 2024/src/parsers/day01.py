from typing import List, Tuple


def parse_from_file(filename: str) -> Tuple[List[int], List[int]]:
    lhs = []
    rhs = []
    with open(filename) as file:
        for line in file:
            parsed_items = [int(item) for item in line.rstrip().split(' ') if item]
            lhs.append(parsed_items[0])
            rhs.append(parsed_items[1])

    return (lhs, rhs)