from structures import *
from game_parser import parse_game
from typing import TextIO

def sum_of_power_of_games(file: TextIO) -> int:
    sum = 0
    while line := file.readline():
        game = parse_game(line)
        sum += game.power()

    return sum

with open('input.txt') as file:
    print(f"sum is {sum_of_power_of_games(file)}")