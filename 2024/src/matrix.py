from dataclasses import dataclass
from typing import Iterable, List, Tuple

@dataclass
class Matrix:
    lhs: List[int]
    rhs: List[int]

    def __init__(self, filename: str):
        self.lhs = []
        self.rhs = []
        
        with open(filename) as file:
            for line in file:
                self.insert([item for item in line.rstrip().split(' ') if item])

    def insert(self, items: List[str]) -> None:
        if len(items) > 2:
            raise ValueError(f"{len(items)=}is greater than 2")
        
        if not items:
            return
        
        self.lhs.append(int(items[0]))
        self.rhs.append(int(items[1]))
    
    def iter_mins(self) -> Iterable[Tuple[int, int]]:
        return MatrixMinIterator(self)

class MatrixMinIterator:
    def __init__(self, matrix: Matrix) -> None:
        self.lhs = sorted(matrix.lhs)
        self.rhs = sorted(matrix.rhs)

    def __iter__(self):
        return self
    
    def __next__(self) -> Tuple[int, int]:
        if not self.lhs:
            raise StopIteration

        return (self.lhs.pop(0), self.rhs.pop(0))
