import importlib

from advent_of_code.shared.solution import Solution


def load_solution(target: tuple[int, int]) -> type[Solution]:
    year, day = target

    module_name = f"advent_of_code.{year}.day{day}"
    class_name = f"Day{day}"

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as exc:
        if exc.name == module_name:
            raise SystemExit(
                f"No solution found for Advent of Code "
                f"{year} Day {day:02}"
            ) from exc
        raise

    try:
        return getattr(module, class_name)
    except AttributeError as exc:
        raise SystemExit(
            f"{module_name} does not contain {class_name}"
        ) from exc
