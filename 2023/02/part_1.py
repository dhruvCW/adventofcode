from structures import *
from game_parser import parse_game
from typing import TextIO

def sum_possible_game_ids(file: TextIO) -> int:
    sum = 0
    expected = Round([Cube(12, Color.RED), Cube(13, Color.GREEN), Cube(14, Color.BLUE)])
    while line := file.readline():
        game = parse_game(line)
        if game.is_possible(expected):
            sum += game.id

    return sum

with open('input.txt') as file:
    print(f"sum is {sum_possible_game_ids(file)}")
