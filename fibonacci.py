"""Generate Fibonacci numbers from the command line."""

import argparse


def fibonacci(count: int) -> list[int]:
    """Return the first `count` Fibonacci numbers, starting with 0, 1."""
    if count < 0:
        raise ValueError("count must be non-negative")

    sequence: list[int] = []
    first, second = 0, 1
    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("count", type=int, help="number of Fibonacci numbers to print")
    args = parser.parse_args()

    try:
        print(*fibonacci(args.count))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
