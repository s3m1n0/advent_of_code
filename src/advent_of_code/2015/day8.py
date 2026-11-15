from aocd import get_data


puzzle_input = get_data(day=8, year=2015)


# no return instructions are global state
def parse(puzzle_input: str) -> list[str]:
    return puzzle_input.splitlines()


def parse_escape_characters(data: str) -> str:
    result = ""
    i = 1  # Skip opening quote

    while i < len(data) - 1:  # Stop before closing quote
        if data[i] != "\\":
            result += data[i]
            i += 1

        else:
            if data[i + 1] == "\\":
                result += "\\"
                i += 2

            elif data[i + 1] == '"':
                result += '"'
                i += 2

            elif data[i + 1] == "x":
                try:
                    result += chr(int(data[i + 2 : i + 4], 16))
                    i += 4
                except ValueError:
                    raise ValueError("invalid numeric value after \\x")
            else:
                raise ValueError("unsupported format")

            # Inspect escape sequence
            # Append decoded character
            # Advance by the appropriate amount

    return result


def part1(data: list[str]) -> int:
    literal_chars = 0
    memory_chars = 0

    for line in data:
        literal_chars += len(line)
        # memory_chars += len(bytes(line, "utf-8").decode("unicode_escape")) - 2
        decoded_line = parse_escape_characters(line)
        memory_chars += len(decoded_line)

    return literal_chars - memory_chars


def part2(data) -> int:
    old_string_count = 0
    new_string_count = 0

    for line in data:
        old_string_count += len(line)

        new_string_count += len(line)
        new_string_count += 2 + line.count("\\") + line.count('"')

    return new_string_count - old_string_count


if __name__ == "__main__":
    data = parse(puzzle_input)
    print(part1(data))
    print(part2(data))
