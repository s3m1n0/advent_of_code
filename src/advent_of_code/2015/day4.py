from aocd import get_data
import hashlib

puzzle_input = get_data(day=4, year=2015)


def parse(puzzle_input: str) -> str:
    return puzzle_input.strip()


def solve(puzzle_input: str, zeros: int) -> int:
    target = "0" * zeros
    encoded_input = puzzle_input.encode()

    i = 0
    while True:
        h = hashlib.md5(encoded_input + str(i).encode()).hexdigest()

        if h.startswith(target):
            return i

        i += 1


def part1(data: str) -> int:
    return solve(data, 5)


def part2(data: str) -> int:
    return solve(data, 6)


if __name__ == "__main__":
    data = parse(puzzle_input)
    print(part1(data))
    print(part2(data))
