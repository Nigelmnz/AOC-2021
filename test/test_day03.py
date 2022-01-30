from src.day03 import answer_1, answer_2, parse_lines
from src.util import get_input

example_input = parse_lines(get_input('test-day03'))
input = parse_lines(get_input('day03'))

def test_example_1():
    assert answer_1(example_input) == 198

def test_solution_1():
    assert answer_1(input) == 3847100

def test_example_2():
    assert answer_2(example_input) == 230

def test_solution_2():
    assert answer_2(input) == 4105235