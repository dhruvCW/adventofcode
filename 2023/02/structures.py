from dataclasses import dataclass
from enum import StrEnum
from sre_constants import MIN_REPEAT_ONE
from typing import List, Iterator

class Color(StrEnum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'


@dataclass
class Cube:
    count: int
    color: Color

@dataclass
class Round:
    cubes: List[Cube]

    def __iter__(self) -> Iterator[Cube]:
        return self.cubes.__iter__()
    
    def select_cube(self, color: Color) -> Cube:
        for cube in self.cubes:
            if cube.color == color:
                return cube
            
        return Cube(0, color)

@dataclass
class Game:
    id: int
    rounds: List[Round]

    def is_possible(self, expected: Round) -> bool:
        for round in self.rounds:
            for expected_cube in expected:
                cube = round.select_cube(expected_cube.color)
                if cube.count > expected_cube.count:
                    return False

        return True
    
    def min_round(self) -> Round:
        minRound = Round([Cube(0, Color.RED), Cube(0, Color.BLUE), Cube(0, Color.GREEN)])
        for round in self.rounds:
            for min_cube in minRound:
                cube = round.select_cube(min_cube.color)
                if cube.count > min_cube.count:
                    min_cube.count = cube.count
                
        return minRound
    
    def power(self) -> int:
        result = 1
        for cube in self.min_round():
            result *= cube.count

        return result