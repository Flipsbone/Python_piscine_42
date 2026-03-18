#!/usr/bin/env python3

def multiple_import() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print("Method 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def aliased_import() -> None:
    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import:")
    print(f"heal(): {heal()}\n")


def spec_function_import() -> None:
    from alchemy.elements import create_water
    print("Method 2 - Specific function import:")
    print(f"create_water(): {create_water()}\n")


def full_import() -> None:
    import alchemy.elements
    print("Method 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}\n")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===\n")
    try:
        full_import()
        spec_function_import()
        aliased_import()
        multiple_import()
    except (AttributeError, ImportError) as e:
        print(f"{e}")

    print("\nAll import transmutation methods mastered!")
