#!/usr/bin/env python3

import alchemy


def main() -> None:

    print("=== Sacred Scroll Mastery ===\n")
    try:
        print("Testing direct module access:")

        print(
            "alchemy.elements.create_fire():", alchemy.elements.create_fire())
        print(
            "alchemy.elements.create_water():",
            alchemy.elements.create_water())
        print(
            "alchemy.elements.create_earth():",
            alchemy.elements.create_earth())
        print(
            "alchemy.elements.create_air():", alchemy.elements.create_air())

    except AttributeError as e:
        print(f"{e}")

    print("\nTesting package-level access (controlled by __init__.py):")

    try:
        print("alchemy.create_fire():",  alchemy.create_fire())
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        print("alchemy.create_water():", alchemy.create_water())
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print("alchemy.create_earth():", alchemy.create_earth())
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print("alchemy.create_air():", alchemy.create_air())
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")

    try:
        print(f"Version: {alchemy.__version__}")
    except AttributeError:
        print("Version: Not defined")

    try:
        print(f"Author: {alchemy.__author__}")
    except AttributeError:
        print("Author: Not defined")


if __name__ == "__main__":
    main()
