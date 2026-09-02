from abc import ABC, abstractmethod

class Solution[T](ABC):
    def __init__(self, data: str):
        self.data: str = data
        self.parsed: T = self.parse()

    @abstractmethod
    def parse(self) -> T:
        ...

    @abstractmethod
    def part1(self) -> int:
        ...

    @abstractmethod
    def part2(self) -> int:
        ...
