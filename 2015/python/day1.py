import os
def read_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "day1.dat")
    with open(file_path) as f:
        return f.read().strip()

def part1(puzzle_input):
    return puzzle_input.count("(") - puzzle_input.count(")")

def part2(puzzle_input):
    floor = 0
    for idx, char in enumerate(puzzle_input, start=1):
        if char == "(":
            floor += 1
        else:
            floor -= 1
    
        if floor == -1:
            return idx
            



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")