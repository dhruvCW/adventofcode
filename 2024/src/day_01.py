from collections import Counter
from functools import reduce
from matrix import Matrix

def total_distance(input: str) -> int:
    matrix = Matrix(input)

    return reduce(lambda distance, items: distance + abs(items[0] - items[1]), matrix.iter_mins(), 0)

def similarity_score(input: str) -> int:
    matrix = Matrix(input)
    rhs_counter = Counter(matrix.rhs)

    return reduce(lambda score, item: score + (item * rhs_counter[item]), matrix.lhs, 0)