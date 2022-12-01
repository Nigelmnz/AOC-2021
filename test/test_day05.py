from src.day05 import answer_1, answer_2, parse_lines
from src.util import get_input

example_input = parse_lines(get_input('test-day05'))
input = parse_lines(get_input('day05'))

def test_parselines():
    assert parse_lines(["1,1 -> 2,2"]) == [((1,1), (2,2))]

def test_example_1():
    assert answer_1(example_input) == 5

def test_solution_1():
    assert answer_1(input) == 5169

def test_example_2():
    assert answer_2(example_input) == 12

def test_solution_2():
    assert answer_2(input) == 22083