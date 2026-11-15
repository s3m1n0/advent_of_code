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
            wire_lookup[operators[3]] = instruction
            continue

        elif operators[1] == "LSHIFT":
            instruction.left = try_number_conversion(operators[0])
            instruction.right = try_number_conversion(operators[2])
            instruction.instruction = "LSHIFT"
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
            instruction.instruction = "AND"
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


signal_cache: dict[str, int] = {}


# this programm walks the children of the root and computes them
def parse_wire(root: str) -> int:

    instruction = wire_lookup[root]

    if isinstance(instruction, int):
        return instruction

    if root in signal_cache:
        return signal_cache[root]

    check_cache = lambda x: signal_cache[x] if x in signal_cache else parse_wire(x)
    check_number = lambda x: x if isinstance(x, int) else check_cache(x)
    result = 0
    match instruction.instruction:
        case "ASSIGNMENT":
            result = check_number(instruction.left)
        case "NOT":
            result = ~check_number(instruction.left) & 0xFFFF
        case "LSHIFT":
            result = check_number(instruction.left) << check_number(instruction.right)
        case "RSHIFT":
            result = check_number(instruction.left) >> check_number(instruction.right)
        case "AND":
            result = check_number(instruction.left) & check_number(instruction.right)
        case "OR":
            result = check_number(instruction.left) | check_number(instruction.right)
        case _:
            raise Exception("unknown operator")

    if isinstance(result, int):
        signal_cache[root] = result
        return result


def part1(target) -> int:
    # find the a wire

    result = parse_wire(target)

    return result


def part2(target) -> int:
    part1_result = 16076
    wire_lookup["b"] = 16076
    signal_cache.clear()
    result = parse_wire(target)

    return result


if __name__ == "__main__":
    data = parse(puzzle_input)

    print(part1("a"))
    print(part2("a"))
