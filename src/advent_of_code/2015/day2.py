import os
def read_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "day2.dat")
    with open(file_path) as f:
        return [
            tuple(map(int, line.strip().split("x"))) for line in f
        ]


def part1(puzzle_input):
    total = 0
    for l, w, h in puzzle_input:
        areas = [h * w, w * l, l * h]
        total += 2 * sum(areas) + min(areas)    


    return total

def part2(puzzle_input):
    total = 0
    for l, w, h in puzzle_input:
        wrap  =  2 * (h + l + w - max(h,l,w))
        total += wrap + h * w * l    


    return total



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")