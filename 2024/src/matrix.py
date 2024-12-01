from dataclasses import dataclass
from typing import Iterable, List, Tuple

def parse_items_from_file(filename: str) -> Iterable[List[int]]:
    with open(filename) as file:
        for line in file:
            yield [int(item) for item in line.rstrip().split(' ') if item]

@dataclass
class Matrix:
    lhs: List[int]
    rhs: List[int]

    def __init__(self, filename: str):
        self.lhs, self.rhs = map(list, zip(*parse_items_from_file(filename)))
        
    
    def iter_mins(self) -> Iterable[Tuple[int, int]]:
        self.__sort()

        for item in zip(self.lhs, self.rhs):
            yield item

    def __sort(self) -> None:
        self.lhs.sort()
        self.rhs.sort()
