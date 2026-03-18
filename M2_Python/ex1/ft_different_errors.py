#!/usr/bin/env python3.10
"""A function that raises different types of errors for demonstration."""


def garden_operations(action: str) -> None:
    """ Perform different garden operations that may raise errors.
    Args:
        action (str): The type of operation to perform.
    Raises:
        ValueError: If the action is 'convert' and conversion fails.
        ZeroDivisionError: If the action is 'divid'and division by zero occurs.
        FileNotFoundError: If the action is 'open' and the file does not exist.
        KeyError: If the action is 'look' and a missing key is accessed.
    """
    if action == "convert":
        int("abc")
    elif action == "divid":
        1 / 0
    elif action == "open":
        open("missing.txt", "r")
    elif action == "look":
        dictionnary: dict[str, str] = {}
        dictionnary["missing_plant"]


def test_error_types() -> None:
    """Test various error types to ensure proper exception handling."""
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        garden_operations("convert")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("divid")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("open")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operations("look")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("convert")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
