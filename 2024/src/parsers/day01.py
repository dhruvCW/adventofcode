from typing import List, Tuple


def parse_from_file(filename: str) -> Tuple[List[int], List[int]]:
    lhs = []
    rhs = []
    with open(filename) as file:
        for line in file:
            parsed_items = [int(item) for item in line.rstrip().split(' ') if item]
            if len(parsed_items) > 2:
                raise ValueError(f"expected {len(parsed_items)=} to be eq to 2")
            
            lhs.append(parsed_items[0])
            rhs.append(parsed_items[1])

    return (lhs, rhs)