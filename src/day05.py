from typing import List, Tuple

Coord = Tuple[int, int]

def answer_1(input: List[Tuple[Coord, Coord]]):
    coords = {}

    for start, end in input:
        x1, y1 = start
        x2, y2 = end
        if x1 == x2 or y1 == y2:
            for y in range(min(y1,y2), max(y1, y2) + 1):
                for x in range(min(x1,x2), max(x1,x2) + 1):
                    if (x,y) not in coords:
                        coords[(x,y)] = 0

                    coords[(x,y)] += 1

    return len([v for v in coords.values() if v >= 2])

def answer_2(input: List[Tuple[Coord, Coord]]):
    coords = {}

    def update_coords(x,y):
        if (x,y) not in coords:
            coords[(x,y)] = 0

        coords[(x,y)] += 1

    for start, end in input:
        x1, y1 = start
        x2, y2 = end

        x, y = x1, y1
        x_dir = ((x2 - x1) // abs(x2 - x1)) if x1 != x2 else 0
        y_dir = ((y2 - y1) // abs(y2 - y1)) if y1 != y2 else 0

        while True:
            update_coords(x,y)
            if x == x2 and y == y2:
                break
            
            x += x_dir
            y += y_dir

    return len([v for v in coords.values() if v >= 2])

def parse_lines(lines) -> List[Tuple[Coord, Coord]]:
    coordPairs = []
    for line in lines:
        coordPair = []
        for coordStr in line.split(' -> '):
            coordPair.append(tuple(int(n) for n in coordStr.split(',')))
        coordPairs.append(tuple(coordPair))

    return coordPairs