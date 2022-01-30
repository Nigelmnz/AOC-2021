from typing import Tuple

def answer_1(input: Tuple[str, int]):
    depth = 0
    position = 0

    for cmd, val in input:
        if cmd == 'forward':
            position += val
        elif cmd == 'down':
            depth += val
        elif cmd == 'up':
            depth -= val

    return depth*position

def answer_2(input: Tuple[str, int]):
    aim = 0
    depth = 0
    position = 0

    for cmd, val in input:
        if cmd == 'forward':
            position += val
            depth += aim*val
        elif cmd == 'down':
            aim += val
        elif cmd == 'up':
            aim -= val

    return depth*position

def parse_lines(lines) -> Tuple[str, int]:
    return [(cmd, int(val)) for [cmd, val] in [line.split() for line in lines]]