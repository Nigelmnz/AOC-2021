from typing import List

InputType = List[int]

def compute( input: InputType, days: int):
    fishestates = {n: 0 for n in range(0, 10)}

    for fish in input:
        fishestates[fish] += 1

    for day in range(days):
        for n in range(0, 10):
            if n == 0:
                fishestates[7] += fishestates[0]
                fishestates[9] += fishestates[0]
            else:
                fishestates[n-1] += fishestates[n]

            fishestates[n] = 0

    return sum(fishestates.values())
    
def answer_1(input: InputType):
    return compute(input, 80)

def answer_2(input: InputType):
    return compute(input, 256)

def parse_lines(lines) -> InputType:
    return [int(n) for n in lines[0].split(',')]