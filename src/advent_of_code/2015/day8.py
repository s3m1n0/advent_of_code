from aocd import get_data


puzzle_input = get_data(day=8, year=2015)


# no return instructions are global state
def parse(puzzle_input: str) -> list[str]:
    return puzzle_input.splitlines()


def part1(data) -> int:
    return 0


def part2(data) -> int:
    return 0


if __name__ == "__main__":
    data = parse(puzzle_input)

    print(part1(data))
    print(part2(data))
