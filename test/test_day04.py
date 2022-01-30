from src.day04 import Board, answer_1, answer_2, parse_lines
from src.util import get_input

example_input = parse_lines(get_input('test-day04'))
input = parse_lines(get_input('day04'))

def test_board():
    board = Board([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
    for n in range(1, 6):
        board.mark(n)

    assert board.win_check() == True
    assert board.unmarked_sum() == 310

def test_example_1():
    assert answer_1(example_input) == 4512

def test_solution_1():
    assert answer_1(input) == 41668

def test_example_2():
    assert answer_2(example_input) == 1924

def test_solution_2():
    assert answer_2(input) == 10478