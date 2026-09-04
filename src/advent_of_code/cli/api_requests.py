from pathlib import Path

import requests


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def read_cookie() -> str:
    return (PROJECT_ROOT / "aoc_session").read_text().strip()


def fetch_puzzle_input(year: int, day: int) -> str:
    try:
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies={"session": read_cookie()},
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError("could not load input data from Advent of Code") from exc

    return response.text


def submit_solution(year: int, day: int, part: int, solution: int) -> bool:
    if part not in (1, 2):
        raise ValueError("part must be 1 or 2")

    try:
        response = requests.post(
            f"https://adventofcode.com/{year}/day/{day}/answer",
            cookies={"session": read_cookie()},
            data={
                "level": part,
                "answer": str(solution),
            },
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError("could not submit solution to Advent of Code") from exc

    # AoC doesn't return a simple JSON success value; the response is HTML.
    # A successful HTTP request therefore isn't necessarily a correct answer.
    return "That's the right answer!" in response.text
