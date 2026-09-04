import argparse
from time import perf_counter

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from advent_of_code.cli.load_solution import load_solution
from advent_of_code.cli.puzzle_input import get_data


console = Console()


def valid_day(value: str) -> int:
    day = int(value)

    if not 1 <= day <= 25:
        raise argparse.ArgumentTypeError(
            "day must be between 1 and 25"
        )

    return day


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run an Advent of Code solution."
    )
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

    args = parser.parse_args()
    target = (args.year, args.day)

    console.print(
        Panel(
            f"[bold cyan]Advent of Code[/bold cyan] "
            f"{args.year} · Day {args.day:02}",
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

    table = Table(title="Solution", expand=False)
    table.add_column("Part", style="cyan")
    table.add_column("Answer", style="green")

    table.add_row("Part 1", str(part1))
    table.add_row("Part 2", str(part2))

    console.print(table)
    console.print(f"[dim]Completed in {elapsed:.2f} ms[/dim]")


if __name__ == "__main__":
    main()
