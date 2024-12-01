from collections import Counter
from parsers.day01 import parse_from_file

def total_distance(input: str) -> int:
    lhs, rhs = map(sorted, parse_from_file(input))

    return sum(abs(lhs - rhs) for lhs, rhs in zip(lhs, rhs))

def similarity_score(input: str) -> int:
    lhs, rhs = parse_from_file(input)
    rhs_counter = Counter(rhs)

    return sum(item * rhs_counter[item] for item in lhs)