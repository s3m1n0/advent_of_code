from typing import override

from advent_of_code.shared.solution import Solution


class Day1(Solution[str]):
    @override
    def parse(self):
        return str(self).strip()

    @override
    def part1(self):
        return self.parsed.count("(") - self.parsed.count(")")

    @override
    def part2(self):
        floor = 0
        for idx, char in enumerate(self.parsed, start=1):
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

            if floor == -1:
                return idx
        raise Exception("elevator never moved under the base floor")
