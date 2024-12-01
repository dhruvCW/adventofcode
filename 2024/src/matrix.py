from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Matrix:
    lhs: List[int]
    rhs: List[int]

    def __init__(self):
        self.lhs = []
        self.rhs = []

    def insert(self, items: List[str]) -> None:
        if len(items) > 2:
            raise ValueError(f"{len(items)=}is greater than 2")
        
        if not items:
            return
        
        self.lhs.append(int(items[0]))
        self.rhs.append(int(items[1]))

    def sort(self) -> None:
        self.lhs.sort()
        self.rhs.sort()
    
    def pop_mins(self) -> Tuple[int, int] | None:
        if not self.lhs:
            return

        return (self.lhs.pop(0), self.rhs.pop(0))



