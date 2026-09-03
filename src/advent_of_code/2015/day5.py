from typing import override

from advent_of_code.shared.solution import Solution

BAD_COMBOS = ("ab", "cd", "pq", "xy")
VOWELS = set("aeiou")


class Day5(Solution[list[str]]):
    @override
    def parse(self) -> list[str]:
        return self.data.splitlines()

    @override
    def part1(self) -> int:
        nice_word_count = 0

        for word in self.parsed:
            word_length = len(word)

            at_least_3_vowels = (char for char in word if char in VOWELS)
            forbidden_combos = (
                word[i] + word[i + 1] in BAD_COMBOS for i in range(word_length - 1)
            )
            letter_appears_twice = (
                word[i] == word[i + 1] for i in range(word_length - 1)
            )

            if (
                not any(forbidden_combos)
                and sum(1 for _ in at_least_3_vowels) >= 3
                and any(letter_appears_twice)
            ):
                nice_word_count += 1

        return nice_word_count

    @override
    def part2(self) -> int:
        nice_word_count = 0

        for word in self.parsed:
            word_length = len(word)

            has_sandwiched_letter = (
                word[i] == word[i + 2] for i in range(word_length - 2)
            )

            has_repeated_pair = False
            seen: dict[str, int] = {}

            for i in range(word_length - 1):
                pair = word[i : i + 2]

                if pair in seen and i - seen[pair] > 1:
                    has_repeated_pair = True

                seen.setdefault(pair, i)

            if has_repeated_pair and any(has_sandwiched_letter):
                nice_word_count += 1

        return nice_word_count
