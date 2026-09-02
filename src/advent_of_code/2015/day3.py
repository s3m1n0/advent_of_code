from typing import override

from advent_of_code.shared.solution import Solution

DIRECTIONS = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}


class Day3(Solution[str]):
    @override
    def parse(self) -> str:
        return self.data.strip()

    @staticmethod
    def move(
        pos: tuple[int, int],
        direction: str,
    ) -> tuple[int, int]:
        x, y = pos
        dx, dy = DIRECTIONS[direction]
        return (x + dx, y + dy)

    @override
    def part1(self) -> int:
        pos = (0, 0)
        visited = {(0, 0)}

        for direction in self.parsed:
            pos = self.move(pos, direction)
            visited.add(pos)

        return len(visited)

    @override
    def part2(self) -> int:
        santa = (0, 0)
        robo = (0, 0)
        visited = {(0, 0)}

        for i, direction in enumerate(self.parsed):
            if i % 2 == 0:
                santa = self.move(santa, direction)
                visited.add(santa)
            else:
                robo = self.move(robo, direction)
                visited.add(robo)

        return len(visited)
