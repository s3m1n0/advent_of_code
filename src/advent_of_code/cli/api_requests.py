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


from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass
class SubmissionResult:
    correct: bool
    message: str


def submit_solution(
    year: int,
    day: int,
    part: int,
    solution: object,
) -> SubmissionResult:
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

    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.find("article")

    if article is None:
        raise RuntimeError("unexpected response from Advent of Code")

    message = article.get_text(" ", strip=True)

    if "That's the right answer!" in message:
        return SubmissionResult(True, message)

    return SubmissionResult(False, message)
