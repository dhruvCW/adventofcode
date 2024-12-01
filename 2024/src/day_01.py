from matrix import Matrix
from typing import List

def read_matrix_from(input) -> Matrix:
    matrix = Matrix()

    with open(input) as file:
        for line in file:
            matrix.insert([item for item in line.rstrip().split(' ') if item])

    return matrix

def frequency(value: int, items: List[int]) -> int:
    count = 0
    
    for item in items:
        if item == value:
            count += 1

    return count
    


def total_distance(input: str) -> int:
    matrix = read_matrix_from(input)
    distance = 0

    matrix.sort()

    while items := matrix.pop_mins():
        distance += abs(items[0] - items[1])

    return distance

def similarity_score(input: str) -> int:
    score = 0
    matrix = read_matrix_from(input)

    for item in matrix.lhs:
        score += item * frequency(item, matrix.rhs)

    return score