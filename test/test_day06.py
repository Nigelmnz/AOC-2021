from src.day06 import answer_1, answer_2, parse_lines
from src.util import get_input

example_input = parse_lines(get_input('test-day06'))
input = parse_lines(get_input('day06'))

def test_example_1():
    print(answer_1(example_input))
    assert answer_1(example_input) == 5934

def test_solution_1():
    assert answer_1(input) == 345387

def test_example_2():
    assert answer_2(example_input) == 26984457539

def test_solution_2():
    assert answer_2(input) == 1574445493136