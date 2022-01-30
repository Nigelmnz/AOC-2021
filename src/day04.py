from typing import List, Tuple

class Board:
    def __init__(self, cells: List[List[int]]):
        self.cells = cells
        self.cell_data = {}

        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                self.cell_data[cell] = {'x': x, 'y': y, 'marked': False}

    def mark(self, number):
        if number in self.cell_data:
            self.cell_data[number]['marked'] = True
    
    def win_check(self):
        win = False

        for row in self.cells:
            win |= all(self.cell_data[n]['marked'] for n in row)
            
        for col in list(zip(*self.cells)):
            win |= all(self.cell_data[n]['marked'] for n in col)

        return win

    def unmarked_sum(self):
        return sum(n for n, data in self.cell_data.items() if not data['marked'])

def answer_1(input: Tuple[List[int], List[Board]]):
    numbers, boards = input
    for n in numbers:
        for board in boards:
            board.mark(n)
            if board.win_check():
                return board.unmarked_sum() * n

def answer_2(input: Tuple[List[int], List[Board]]):
    numbers, boards = input

    remaining = boards
    for n in numbers:
        next_remaining = []
        for i, board in enumerate(remaining):
            board.mark(n)
            if not board.win_check():
                next_remaining.append(board)
            elif len(remaining) == 1:
                return board.unmarked_sum() * n

        remaining = next_remaining

def parse_lines(lines) -> Tuple[List[int], List[Board]]:
    numbers = [int(n) for n in lines[0].split(',')]
    boards = []

    line = 2
    while line < len(lines):
        parsed_rows = [[int(n) for n in row.split()] for row in lines[line:line+5]]
        line += 6
        boards.append(Board(parsed_rows))

    return (numbers, boards)