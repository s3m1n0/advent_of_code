import os
def read_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "..", "data", "day3.dat")
    with open(file_path) as f:
        return f.read().strip()

DIRECTIONS = {
    ">" : (1 , 0),
    "<" : (-1 , 0),
    "^" : (0 , 1),
    "v" : (0 , -1)
}


def move(pos, direction):
    x,y = pos
    dx,dy = DIRECTIONS[direction]
    return (x + dx , y + dy)

def part1(puzzle_input):
    pos = (0,0)
    visited = {(0, 0)}
    for direction in puzzle_input:
       pos = move(pos , direction)
       visited.add(pos)
    return len(visited)

def part2(puzzle_input):
    santa, robo = (0,0), (0,0)
    visited = {(0, 0)}
    for i,direction in enumerate(puzzle_input):
        if i % 2 == 0:
            santa = move(santa, direction)
            visited.add(santa)
        else:
            robo = move(robo , direction)
            visited.add(robo)
    return len(visited)

    



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")