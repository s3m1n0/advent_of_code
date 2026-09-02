import hashlib
from typing import override

from advent_of_code.shared.solution import Solution


class Day4(Solution[str]):
    @override
    def parse(self) -> str:
        return self.data.strip()

    @staticmethod
    def solve(puzzle_input: str, zeros: int) -> int:
        target = "0" * zeros
        encoded_input = puzzle_input.encode()

        i = 0
        while True:
            h = hashlib.md5(
                encoded_input + str(i).encode()
            ).hexdigest()

            if h.startswith(target):
                return i

            i += 1

    @override
    def part1(self) -> int:
        return self.solve(self.parsed, 5)

    @override
    def part2(self) -> int:
        return self.solve(self.parsed, 6)
