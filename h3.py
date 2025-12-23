"""
check_natural.py

Simple utility to check whether a given number is a natural number.
By default natural numbers are considered 1, 2, 3, ... (zero excluded).
Use --include-zero to treat 0 as a natural number.
"""
from __future__ import annotations

import argparse
from typing import Union

Number = Union[int, float]


def is_natural_number(value: Union[str, Number], include_zero: bool = False) -> bool:
    """Return True if value is a natural number.

    Accepts strings, ints, and floats. Floats are considered natural only if they
    are whole numbers (e.g., 3.0).

    Args:
        value: the value to test (e.g., '5', 3, 4.0)
        include_zero: whether to treat 0 as a natural number (default: False)

    Returns:
        bool: True if value is natural, False otherwise
    """
    # Try to convert strings to a number
    if isinstance(value, str):
        value = value.strip()
        try:
            if "." in value:
                num = float(value)
            else:
                num = int(value)
        except ValueError:
            return False
    else:
        num = value

    # Must be int-like
    if isinstance(num, float):
        if not num.is_integer():
            return False
        num = int(num)

    if not isinstance(num, int):
        return False

    if include_zero:
        return num >= 0
    return num >= 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Check whether a number is natural or not")
    parser.add_argument("number", nargs="?", help="Number to check (if omitted, you'll be prompted)")
    parser.add_argument("--include-zero", "-z", action="store_true", help="Treat 0 as a natural number")
    args = parser.parse_args()

    if args.number is None:
        try:
            args.number = input("Enter a number to check: ")
        except EOFError:
            print("No input provided. Exiting.")
            return

    result = is_natural_number(args.number, include_zero=args.include_zero)
    name = "natural number" if args.include_zero else "natural number"
    if result:
        print(f"Yes — {args.number} is a {name}.")
    else:
        print(f"No — {args.number} is not a {name}.")


if __name__ == "__main__":
    main()
