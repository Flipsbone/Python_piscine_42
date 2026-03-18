#!/usr/bin/env python3
"""Module simulating plant growth over a week."""


class Plant:
    """
    Blueprint for a plant that can grow and age.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        age (int): The age in days.
        start_height (int): Track first value of height
    """
    def __init__(self, name: str, height: int, start_age: int) -> None:
        """Initialize a new Plant instance.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
        """
        self.name = name
        self.height = height
        self.start_age = start_age
        self.start_height = height

    def age(self) -> None:
        """Increment the plant's age by one day."""
        self.start_age += 1

    def grow(self, add_cm: int = 1) -> None:
        """Increase the plant's height.
        Args:
            add_cm (int): The number of centimeters to add to the height.
        """
        self.height += add_cm

    def get_info(self) -> str:
        """Return a formatted string of the plant's status."""
        return f"{self.name}: {self.height}cm, {self.start_age} days old"


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    for day in range(1, 8):
        if day == 1 or day == 7:
            print(f"=== Day {day} ===")
            print(rose.get_info())
        if day < 7:
            rose.grow(1)
            rose.age()

    total_height = rose.height - rose.start_height
    print(f"Growth this week: + {total_height}cm")
