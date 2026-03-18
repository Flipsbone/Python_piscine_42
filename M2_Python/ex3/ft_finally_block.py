#!/usr/bin/env python3.10
"""A demonstration of the finally block in exception handling for
garden watering."""


def water_plants(plant_list: list[str]) -> None:
    """Water a list of plants, ensuring cleanup with a finally block.
    Args:
        plant_list (list[str]): A list of plant names to water.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            try:
                print("Watering " + plant)
            except TypeError:
                print(f"Error: Cannot water {plant} - invalid plant!")
                return
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with and without errors."""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    plant_list2 = ["tomato", None, "carrots"]
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
