#!/usr/bin/env python3.10
""" A function that raises ValueError for invalid plant health checks."""


def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int) -> str:
    """Check the health of a plant based on water level and sunlight hours.
    Args:
        plant_name (str): The name of the plant.
        water_level (int): The water level for the plant (1-10).
        sunlight_hours (int): The number of sunlight hours per day (2-12).
    Raises:
        ValueError: If any of the parameters are out of acceptable ranges.
    """
    if not plant_name.strip():
        raise ValueError("Plant name cannot be empty")
    if (water_level < 1):
        raise ValueError(
            f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(
            f"Water level {water_level} is too high (max 10)")
    if (sunlight_hours < 2):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif (sunlight_hours > 12):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    """Test various plant health checks to ensure proper exception raising."""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("Tomato", 5, 6))
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad water level...")
    try:
        check_plant_health("Tomato", 15, 6)
    except ValueError as e:
        print(f"Error: {e}\n")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
