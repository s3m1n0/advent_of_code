from typing import override

from advent_of_code.shared.solution import Solution

type Dimension = tuple[int, int, int]


class Day2(Solution[list[Dimension]]):
    @override
    def parse(self) -> list[tuple[int, int, int]]:
        result: list[tuple[int, int, int]] = []

        for line in self.data.splitlines():
            l, w, h = map(int, line.split("x"))
            result.append((l, w, h))

        return result

    @override
    def part1(self) -> int:
        total = 0

        for l, w, h in self.parsed:
            areas = [h * w, w * l, l * h]
            total += 2 * sum(areas) + min(areas)

        return total

    @override
    def part2(self) -> int:
        total = 0

        for l, w, h in self.parsed:
            wrap = 2 * (h + l + w - max(h, l, w))
            total += wrap + h * w * l

        return total
