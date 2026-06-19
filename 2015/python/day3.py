def read_data():
    with open("../data/day3.dat") as f:
        return f.read().strip()

MOVES = {
    ">" : (1 , 0),
    "<" : (-1 , 0),
    "^" : (0 , 1),
    "v" : (0 , -1)
}


def move(turn, direction):
    if direction not in MOVES:
        raise ValueError("invalid character")
    x,y = turn
    dx,dy = MOVES[direction]
    return (x + dx , y + dy)

def part1(puzzle_input):
    x, y = 0, 0
    visited = {(0, 0)}
    for direction in puzzle_input:
       x,y = move((x,y) , direction)
       visited.add((x, y))
    return len(visited)

def part2(puzzle_input):
    positions = [(0,0), (0,0)]
    visited = {(0, 0)}
    for i,direction in enumerate(puzzle_input):
        idx = i % 2
        turn = positions[idx]
        positions[idx] = move(turn, direction)
        visited.add(positions[idx])
    return len(visited)

    



if __name__ == "__main__":
    data = read_data()
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")