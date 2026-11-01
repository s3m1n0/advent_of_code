from aocd import get_data

puzzle_input = get_data(day=1, year=2015)


def part1(data: str):
    return data.count("(") - data.count(")")


def part2(data):
    floor = 0
    for idx, char in enumerate(data, start=1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return idx
    raise Exception("elevator never moved under the base floor")


if __name__ == "__main__":
    print(part1(puzzle_input))
    print(part2(puzzle_input))
