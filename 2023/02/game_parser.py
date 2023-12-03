from structures import *
import pytest

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
''' 
def parse_game(line: str) -> Game:
    first, second = line.split(':')
    return Game(int(first.split(' ')[-1]), parse_rounds(second.strip()))

'''
3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
'''
def parse_rounds(lines: str) -> List[Round]:
    return [Round(parse_cubes(line.strip())) for line in lines.split(';')]

'''
3 blue, 4 red
'''
def parse_cubes(lines: str) -> List[Cube]:
    return [parse_cube(line.strip()) for line in lines.split(',')]

'''
3 blue
'''
def parse_cube(line: str) -> Cube:
    first, second = line.split(' ')
    return Cube(int(first.strip()), second.strip())

def test_game_parser():
    input = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    ExpectedGame = Game(1, [
        Round([Cube(3, 'blue'), Cube(4, 'red')]), 
        Round([Cube(1, 'red'), Cube(2, 'green'), Cube(6, 'blue')]), 
        Round([Cube(2, 'green')])
        ])

    assert parse_game(input) == ExpectedGame