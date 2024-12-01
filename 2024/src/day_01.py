from collections import Counter
from matrix import Matrix

def total_distance(input: str) -> int:
    matrix = Matrix(input)

    return sum(abs(lhs - rhs) for lhs, rhs in matrix.iter_mins())

def similarity_score(input: str) -> int:
    matrix = Matrix(input)
    rhs_counter = Counter(matrix.rhs)

    return sum(item * rhs_counter[item] for item in matrix.lhs)