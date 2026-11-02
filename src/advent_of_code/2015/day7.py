from aocd import get_data

puzzle_input = get_data(day=7, year=2015)

KEYWORDS = {"NOT", "AND", "LSHIFT", "RSHIFT"}


def parse(puzzle_input): ...


def part1(data) -> int:
    return 0


def part2(data) -> int:
    return 0


if __name__ == "__main__":
    data = parse(puzzle_input)

    print(part1(data))
    print(part2(data))
