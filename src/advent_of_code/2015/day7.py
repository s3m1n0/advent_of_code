from aocd import get_data

from dataclasses import dataclass

puzzle_input = get_data(day=7, year=2015)


def parse(puzzle_input) -> list[int | str | tuple[list[int | str], str, str]]:
    result = []
    try_number_conversion = lambda x: int(x) if x.isdigit() else x
    for line in puzzle_input.splitlines():
        operators = line.split(" ")

        if len(operators) == 3:
            result.append(
                (
                    try_number_conversion(operators[0]),
                    operators[2],
                    "ASSIGN",
                )
            )

        elif len(operators) == 4:
            result.append((try_number_conversion(operators[1]), operators[3], "NOT"))

        elif operators[1] == "LSHIFT":
            result.append(
                (
                    [
                        try_number_conversion(operators[0]),
                        try_number_conversion(operators[2]),
                    ],
                    operators[-1],
                    "LSHIFT",
                )
            )
        elif operators[1] == "RSHIFT":
            result.append(
                (
                    [
                        try_number_conversion(operators[0]),
                        try_number_conversion(operators[2]),
                    ],
                    operators[-1],
                    "RSHIFT",
                )
            )
        elif operators[1] == "AND":
            result.append(
                (
                    [
                        try_number_conversion(operators[0]),
                        try_number_conversion(operators[2]),
                    ],
                    operators[-1],
                    "AND",
                )
            )

        elif operators[1] == "OR":
            result.append(
                (
                    [
                        try_number_conversion(operators[0]),
                        try_number_conversion(operators[2]),
                    ],
                    operators[-1],
                    "OR",
                )
            )
        else:
            print("bad line")
        print(f"{line} just added: {result[-1]}")

    return result


def part1(data) -> int:

    return 0


def part2(data) -> int:
    return 0


if __name__ == "__main__":
    data = parse(puzzle_input)

    print(part1(data))
    print(part2(data))
