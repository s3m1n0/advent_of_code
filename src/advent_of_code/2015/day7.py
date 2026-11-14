from aocd import get_data


class InstructionNode:
    def __init__(self):
        self.instruction: str = ""
        self.left: int | str | None = None
        self.right: int | str | None = None


wire_lookup: dict[str, InstructionNode | int] = {}

puzzle_input = get_data(day=7, year=2015)


# no return instructions are global state
def parse(puzzle_input):
    try_number_conversion = lambda x: int(x) if x.isdigit() else x
    for line in puzzle_input.splitlines():
        instruction = InstructionNode()
        operators = line.split(" ")

        # ASSIGMENT operator
        if len(operators) == 3:
            if operators[0].isdigit():
                wire_lookup[operators[2]] = int(operators[0])
                continue

            instruction.left = try_number_conversion(operators[0])
            instruction.instruction = "ASSIGNMENT"

            wire_lookup[operators[2]] = instruction
            continue

        # NOT operator
        elif len(operators) == 4:
            instruction.left = try_number_conversion(operators[1])
            instruction.instruction = "NOT"
            wire_lookup[operators[2]] = instruction
            continue

        elif operators[1] == "LSHIFT":
            instruction.left = try_number_conversion(operators[0])
            instruction.right = try_number_conversion(operators[2])
            instruction.instruction = ("LSHIFT",)
            wire_lookup[operators[-1]] = instruction
            continue

        elif operators[1] == "RSHIFT":
            instruction.left = try_number_conversion(operators[0])
            instruction.right = try_number_conversion(operators[2])
            instruction.instruction = "RSHIFT"
            wire_lookup[operators[-1]] = instruction
            continue

        elif operators[1] == "AND":
            instruction.left = try_number_conversion(operators[0])
            instruction.right = try_number_conversion(operators[2])
            instruction.instruction = ("AND",)
            wire_lookup[operators[-1]] = instruction
            continue
        elif operators[1] == "OR":
            instruction.left = try_number_conversion(operators[0])
            instruction.right = try_number_conversion(operators[2])
            instruction.instruction = "OR"
            wire_lookup[operators[-1]] = instruction
            continue
        else:
            print("bad line")


def parse_root(instruction: InstructionNode) -> int:
    match instruction.instruction:
        case "ASSIGNMENT":
            ...
        case "NOT":
            ...
        case "LSHIFT":
            ...
        case "RSHIFT":
            ...
        case "AND":
            ...
        case "OR":
            ...
    return 5


def part1(data) -> int:
    # find the a wire

    root = wire_lookup["a"]

    print(root)

    return 0


def part2(data) -> int:
    return 0


if __name__ == "__main__":
    data = parse(puzzle_input)

    print(part1(data))
    print(part2(data))
