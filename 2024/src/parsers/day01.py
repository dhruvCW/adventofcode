from typing import List, Tuple


def parse_from_file(filename: str) -> Tuple[List[int], List[int]]:
    lhs = []
    rhs = []
    with open(filename) as file:
        for line in file:
            first, second = [int(item) for item in line.split()]
            lhs.append(first)
            rhs.append(second)

    return (lhs, rhs)