from src.day02 import answer_1, answer_2, parse_lines
from src.util import get_input

example_input = parse_lines(get_input('test-day02'))
input = parse_lines(get_input('day02'))

def test_example_1():
    assert answer_1(example_input) == 150

def test_solution_1():
    assert answer_1(input) == 2187380

def test_example_2():
    assert answer_2(example_input) == 900

def test_solution_2():
    assert answer_2(input) == 2086357770