from hashlib import sha256
from pathlib import Path
import sqlite3

from advent_of_code.cli.api_requests import fetch_puzzle_input
from rich.console import Console


DB_PATH = Path(__file__).resolve().parents[3] / "aoc_cache.db"


def hash_target(year: int, day: int) -> str:
    value = f"{year}:{day}"
    return sha256(value.encode()).hexdigest()


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS puzzle_inputs (
                hash_id TEXT PRIMARY KEY,
                input TEXT NOT NULL
            )
        """)


def search_input_in_db(hash_id: str) -> str | None:
    with sqlite3.connect(DB_PATH) as db:
        row = db.execute(
            "SELECT input FROM puzzle_inputs WHERE hash_id = ?",
            (hash_id,),
        ).fetchone()

    return row[0] if row else None


def check_cache(year: int, day: int) -> str | None:
    hash_id = hash_target(year, day)
    return search_input_in_db(hash_id)


def cache_input(year: int, day: int, data: str) -> None:
    hash_id = hash_target(year, day)

    with sqlite3.connect(DB_PATH) as db:
        db.execute(
            """
            INSERT OR REPLACE INTO puzzle_inputs (hash_id, input)
            VALUES (?, ?)
            """,
            (hash_id, data),
        )


def get_data(target: tuple[int, int]) -> str:
    init_db()
    year, day = target
    console = Console()


    if data := check_cache(year, day):
        console.print("[green]✓[/green] Puzzle input loaded from cache")
        return data

    console.print("[yellow]↓[/yellow] Downloading puzzle input...")
    data = fetch_puzzle_input(year, day)
    cache_input(year, day, data)

    return data
