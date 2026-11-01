from aocd import get_data

puzzle_input = get_data(day=2, year=2015)


def parse(puzzle_input: str) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []

    for line in puzzle_input.splitlines():
        l, w, h = map(int, line.split("x"))
        result.append((l, w, h))

    return result


def part1(data: list[tuple[int, int, int]]) -> int:
    total = 0

    for l, w, h in data:
        areas = [h * w, w * l, l * h]
        total += 2 * sum(areas) + min(areas)

    return total


def part2(data: list[tuple[int, int, int]]) -> int:
    total = 0

    for l, w, h in data:
        wrap = 2 * (h + l + w - max(h, l, w))
        total += wrap + h * w * l

    return total


if __name__ == "__main__":
    data = parse(puzzle_input)
    print(part1(data))
    print(part2(data))
