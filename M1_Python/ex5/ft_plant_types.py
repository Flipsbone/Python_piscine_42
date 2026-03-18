#!/usr/bin/env python3
"""Module defining a hierarchy of specialized garden plants."""


class Plant:
    """
    Blueprint for a plant that can grow and age.
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
        else:
            self.__height = height

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

    def get_height(self) -> int:
        """Return the protected height."""
        return self.__height

    def get_age(self) -> int:
        """Return the protected age."""
        return self.__age

    def display_status(self) -> None:
        """Display current status with exact subject formatting."""
        print(f"{self.name} ({type(self).__name__}): {self.get_height()}cm,"
              f" {self.get_age()} days, ", end="")


class Flower(Plant):
    """
    Specialized plant type that can bloom and has a color.
    Attributes:
        color (str): The color of the plant.
        Inherited attributes (name,height,age) are managed by the Plant class.
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize flower with color and inherited plant attributes.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
            color (str): The color of the plant.
        """
        super().__init__(name, height, age)
        """ Initialize flower with color and inherited plant attributes.
         Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
            color (str): The color of the plant.
         """
        self.color = color

    def display_status(self) -> None:
        """Display flower-specific status and color and blooming action."""
        super().display_status()
        print(f"{self.color} color")
        self.bloom()

    def bloom(self) -> None:
        """Print a message indicating the flower is blooming."""
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """
    Specialized plant type that provides shade based on trunk diameter.
    Attributes:
        trunk_diameter (int): The trunk of the tree.
        Inherited attributes (name,height,age) are managed by the Plant class.
    """
    def __init__(
            self, name: str, height: int, age: int,
            trunk_diameter: int) -> None:
        """Initialize tree with trunk diameter and inherited plant attributes.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
            trunk_diameter (int): The trunk of the tree.
        """
        super().__init__(name, height, age)
        """ Initialize tree with trunk diameter and inherited plant attributes.
         Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
            trunk_diameter (int): The trunk of the tree.
         """
        self.set_trunk_diameter(trunk_diameter)

    def set_trunk_diameter(self, trunk_diameter: int) -> None:
        """Validate and set trunk diameter.
        Args:
            trunk_diameter (int): The trunk of the tree.
        """
        if trunk_diameter > 0:
            self.__trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> int:
        """Return the protected trunk diameter."""
        return self.__trunk_diameter

    def display_status(self) -> None:
        """Display tree-specific status including diameter and shade area."""
        super().display_status()
        print(f"{self.get_trunk_diameter()}cm diameter")
        self.produce_shade()

    def produce_shade(self) -> None:
        '''Calculate and print the shade area provided by the tree.'''
        d_trunk_m = self.__trunk_diameter / 100
        d_crown_m = d_trunk_m * 20
        radius_m = d_crown_m / 2
        shade = 3.14 * (radius_m ** 2)
        print(f"{self.name} provides {shade:.0f} square meters of shade\n")


class Vegetable(Plant):
    """
    Specialized plant type representing food crops.
        Attributes:
        harvest_season (str): The season when the vegetable is harvested.
        nutritional_value (str): The key vitamin provided by the vegetable.
        Inherited attributes (name,height,age) are managed by the Plant class.
    """
    def __init__(
        self, name: str, height: int,
        age: int, harvest_season: str, nutritional_value: str
    ) -> None:
        """Initialize vegetable with harvest season, nutrition, and inherited
        plant attributes.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
            harvest_season (str): The season when the vegetable is harvested.
            nutritional_value (str): The key vitamin provided by the vegetable.
        """
        super().__init__(name, height, age)
        """ Initialize vegetable with harvest season, nutrition, and inherited
         plant attributes.
         Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            age (int): The age in days.
            harvest_season (str): The season when the vegetable is harvested.
            nutritional_value (str): The key vitamin provided by the vegetable.
         """
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value.capitalize()

    def display_status(self) -> None:
        """Display vegetable-specific status and harvest season + nutrition."""
        super().display_status()
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    garden_center = [
        Flower("rose", 25, 30, "red"),
        Tree("oak", 500, 1825, 50),
        Vegetable("tomato", 80, 90, "summer", "c"),
        Flower("lily", 15, 12, "white"),
        Tree("pine", 300, 730, 20),
        Vegetable("bean", 40, 45, "spring", "b"),
    ]

    for my_plant in garden_center:
        my_plant.display_status()
