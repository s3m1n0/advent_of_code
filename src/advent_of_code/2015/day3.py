from aocd import get_data

puzzle_input = get_data(day=3, year=2015)

DIRECTIONS = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}


def parse(puzzle_input: str) -> str:
    return puzzle_input.strip()


def move(
    pos: tuple[int, int],
    direction: str,
) -> tuple[int, int]:
    x, y = pos
    dx, dy = DIRECTIONS[direction]
    return (x + dx, y + dy)


def part1(data: str) -> int:
    pos = (0, 0)
    visited = {(0, 0)}

    for direction in data:
        pos = move(pos, direction)
        visited.add(pos)

    return len(visited)


def part2(data: str) -> int:
    santa = (0, 0)
    robo = (0, 0)
    visited = {(0, 0)}

    for i, direction in enumerate(data):
        if i % 2 == 0:
            santa = move(santa, direction)
            visited.add(santa)
        else:
            robo = move(robo, direction)
            visited.add(robo)

    return len(visited)


if __name__ == "__main__":
    data = parse(puzzle_input)
    print(part1(data))
    print(part2(data))
