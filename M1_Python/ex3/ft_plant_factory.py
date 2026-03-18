#!/usr/bin/env python3
"""Module providing a factory function to create Plant instances."""


class Plant:
    """
    Blueprint representing a plant in the garden.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        age (int): The age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a new Plant instance.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
        """
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory(name: str) -> Plant:
    """Factory function to create Plant instances based on species name.
    Args:
        name (str): The species name of the plant.
    Returns:
        Plant: A new Plant instance with predefined attributes.
    """
    plant_dictionnary = {
        "Rose": (25, 30),
        "Oak": (200, 365),
        "Cactus": (5, 90),
        "Sunflower": (80, 45),
        "Fern": (15, 120),
    }
    height, age = plant_dictionnary.get(name, (0, 0))
    return Plant(name, height, age)


if __name__ == "__main__":
    plants_names = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
    plants = [ft_plant_factory(name) for name in plants_names]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, "
              f"{plant.age} days)")
    print("\nTotal plants created:", len(plants))
