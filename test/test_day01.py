from src.day01 import answer_1, answer_2, parse_lines
from src.util import get_input

example_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
input = parse_lines(get_input('day01'))

def test_example_1():
    assert answer_1(example_input) == 7

def test_solution_1():
    assert answer_1(input) == 1390

def test_example_2():
    assert answer_2(example_input) == 5

def test_solution_2():
    assert answer_2(input) == 1457