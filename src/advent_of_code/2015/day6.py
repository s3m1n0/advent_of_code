from aocd import get_data

puzzle_input = get_data(day=6, year=2015)

type Instruction = tuple[
    str,
    tuple[int, int],
    tuple[int, int],
]


def parse(puzzle_input: str) -> list[Instruction]:
    instructions = []

    for instruction in puzzle_input.splitlines():
        if instruction.startswith("turn off"):
            op = "off"
            coords = instruction[len("turn off") :]
        elif instruction.startswith("turn on"):
            op = "on"
            coords = instruction[len("turn on") :]
        else:
            op = "switch"
            coords = instruction[len("toggle") :]

        start, end = coords.strip().split(" through ")
        x1, y1 = map(int, start.split(","))
        x2, y2 = map(int, end.split(","))

        instructions.append((op, (x1, y1), (x2, y2)))

    return instructions


def generate_coords(
    start: tuple[int, int],
    end: tuple[int, int],
):
    x1, y1 = start
    x2, y2 = end

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            yield x, y


def part1(data: list[Instruction]) -> int:
    grid = [[False] * 1000 for _ in range(1000)]

    for op, start, end in data:
        for x, y in generate_coords(start, end):
            match op:
                case "off":
                    grid[x][y] = False
                case "on":
                    grid[x][y] = True
                case "switch":
                    grid[x][y] = not grid[x][y]

    return sum(row.count(True) for row in grid)


def part2(data: list[Instruction]) -> int:
    grid = [[0] * 1000 for _ in range(1000)]

    for op, start, end in data:
        for x, y in generate_coords(start, end):
            match op:
                case "off":
                    grid[x][y] = max(0, grid[x][y] - 1)
                case "on":
                    grid[x][y] += 1
                case "switch":
                    grid[x][y] += 2

    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    data = parse(puzzle_input)
    print(part1(data))
    print(part2(data))
