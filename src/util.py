def get_input(filename):
    lines = []
    with open(f'./src/inputs/{filename}.txt') as f:
        lines = [line.strip() for line in f]
    return lines