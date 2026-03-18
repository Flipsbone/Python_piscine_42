#!/usr/bin/env python3.10
"""A demonstration of custom exception classes for garden-related errors."""


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        is_wilting = True
        if is_wilting:
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        print("Testing WaterError...")
        water_tank = 0
        if water_tank <= 0:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        if is_wilting:
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        if water_tank <= 0:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
