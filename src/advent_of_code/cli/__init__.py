import argparse
from time import perf_counter

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from advent_of_code.cli.api_requests import submit_solution
from advent_of_code.cli.load_solution import load_solution
from advent_of_code.cli.puzzle_input import get_data


console = Console()


def valid_day(value: str) -> int:
    day = int(value)

    if not 1 <= day <= 25:
        raise argparse.ArgumentTypeError("day must be between 1 and 25")

    return day


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an Advent of Code solution.")

    parser.add_argument(
        "-y",
        "--year",
        type=int,
        required=True,
        help="Advent of Code year",
    )

    parser.add_argument(
        "-d",
        "--day",
        type=valid_day,
        required=True,
        help="Advent of Code day (1-25)",
    )

    parser.add_argument(
        "-s",
        "--submit",
        action="store_true",
        help="Submit the solutions to Advent of Code",
    )

    args = parser.parse_args()
    target = (args.year, args.day)

    console.print(
        Panel(
            f"[bold cyan]Advent of Code[/bold cyan] {args.year} · Day {args.day:02}",
            expand=False,
        )
    )

    start = perf_counter()

    try:
        data = get_data(target)
        solution = load_solution(target)
        solver = solution(data)

        part1 = solver.part1()
        part2 = solver.part2()

    except (RuntimeError, SystemExit) as exc:
        console.print(f"[bold red]✗[/bold red] {exc}")
        raise SystemExit(1) from exc

    elapsed = (perf_counter() - start) * 1000

    part1_status = ""
    part2_status = ""

    if args.submit:
        try:
            part1_correct = submit_solution(
                args.year,
                args.day,
                1,
                part1,
            )

            part1_status = "✓ Correct" if part1_correct else "✗ Incorrect"

            part2_correct = submit_solution(
                args.year,
                args.day,
                2,
                part2,
            )

            part2_status = "✓ Correct" if part2_correct else "✗ Incorrect"

        except RuntimeError as exc:
            console.print(f"[bold red]✗[/bold red] {exc}")
            raise SystemExit(1) from exc

    table = Table(title="Solution", expand=False)

    table.add_column("Part", style="cyan")
    table.add_column("Answer", style="green")

    if args.submit:
        table.add_column("Submission")

    rows = [
        ("Part 1", str(part1), part1_status),
        ("Part 2", str(part2), part2_status),
    ]

    for part, answer, status in rows:
        if args.submit:
            table.add_row(part, answer, status)
        else:
            table.add_row(part, answer)

    console.print(table)
    console.print(f"[dim]Completed in {elapsed:.2f} ms[/dim]")


if __name__ == "__main__":
    main()
