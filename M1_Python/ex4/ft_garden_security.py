#!/usr/bin/env python3
"""Module protecting plant data integrity through encapsulation."""


class SecurePlant:
    """
    Blueprint representing a plant in the garden.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        age (int): The age in days.
    """
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        """Initialize plant and set initial values through secure methods.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
        """
        print("Plant created:", name.capitalize())
        self.name = name.capitalize()
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        """Validate and set height if non-negative.
        Args:
            height (int): The height in centimeters.
        """
        if height < 0:
            print(
                "Invalid operation attempted: "
                f"height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [ok]")

    def get_height(self) -> int:
        """Return the protected height."""
        return self.__height

    def set_age(self, age: int) -> None:
        """Validate and set age if non-negative.
        Args:
            age (int): The age in days.
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {age} days [ok]\n")

    def get_age(self) -> int:
        """Return the protected age."""
        return self.__age

    def display_status(self) -> None:
        """Display current status with exact subject formatting."""
        print(f"Current plant: {self.name} ({self.get_height()}cm,"
              f" {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    flower = SecurePlant("rose", 25, 30)
    flower.set_height(-5)
    flower.display_status()
