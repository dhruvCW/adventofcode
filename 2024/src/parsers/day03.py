
from dataclasses import dataclass
from re import Match, compile
from typing import Iterable


@dataclass
class Operation:
    instruction: str
    x: int = 0
    y: int = 0

    def __init__(self, match: Match):
        self.instruction = match.group('instruction')
        if self.instruction == 'mul':
            self.x = int(match.group('x'))
            self.y = int(match.group('y'))

def parse_from_file(filename: str) -> Iterable[Operation]:
    pattern = compile(r"(?P<instruction>mul|don't|do)\((?P<x>\d{1,3})?,?(?P<y>\d{1,3})?\)")

    with open(filename) as file:
        for line in file:
            for match in pattern.finditer(line):
                yield Operation(match)