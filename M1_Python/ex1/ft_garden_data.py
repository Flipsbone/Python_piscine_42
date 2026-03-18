#!/usr/bin/env python3
"""Module to manage and display garden plant data."""


class Plant:
    """
    Blueprint representing a plant in the garden.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        age (int): The age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a new Plant instance.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def display(self) -> None:
        """Print the plant's information in the required format."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    list_plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    for plant in list_plants:
        plant.display()
