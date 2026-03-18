#!/usr/bin/env python3
import alchemy.transmutation
from alchemy.transmutation import philosophers_stone, elixir_of_life
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem


def package_access():
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def relative_imports():

    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone(): "
          f"{philosophers_stone()}")
    print("elixir_of_life(): "
          f"{elixir_of_life()}")


def absolute_imports() -> None:
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    try:
        absolute_imports()
        relative_imports()
        package_access()
    except (AttributeError, ImportError) as e:
        print(f"{e}")
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
