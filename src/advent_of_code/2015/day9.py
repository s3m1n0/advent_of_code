from aocd import get_data


puzzle_input = get_data(day=9, year=2015)


# no return instructions are global state
def parse(puzzle_input: str) -> dict[str, list[tuple[str, int]]]:
    adjacency_list: dict[str, list[tuple[str, int]]] = {}
    for line in puzzle_input.splitlines():
        elements = line.split()
        city1 = elements[0]
        city2 = elements[2]
        weight = elements[4]
        if city1 in adjacency_list:
            adjacency_list[city1].append((city2, int(weight)))
        else:
            adjacency_list[city1] = [(city2, int(weight))]

        if city2 in adjacency_list:
            adjacency_list[city2].append((city1, int(weight)))
        else:
            adjacency_list[city2] = [(city1, int(weight))]

    return adjacency_list


def part1(data: list[str]) -> int:
    return 0


def part2(data) -> int:
    return 0


if __name__ == "__main__":
    data = parse(puzzle_input)
    print(part1(data))
    print(part2(data))
