#!/usr/bin/env python3.10
"""A garden management system with custom exceptions and error handling."""


class GardenError(Exception):
    """Base exception class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for plant-related errors in the garden."""
    pass


class WaterError(GardenError):
    """Exception raised for water-related errors in the garden."""
    pass


class Plant:
    """A class representing a plant in the garden.
    Attributes:
        name (str): The name of the plant.
        water_level (int): The water level of the plant.
        sun (int): The sunlight hours the plant receives.
    """
    def __init__(self, name: str, water_level: int, sun: int) -> None:
        """Initialize a Plant instance.
        Args:
            name (str): The name of the plant.
            water_level (int): The water level of the plant.
            sun (int): The sunlight hours the plant receives.
        """
        self.name = name
        self.water_level = int(water_level)
        self.sunlight_hours = sun


class GardenManager:
    """A class to manage garden operations with error handling.
    Attributes:
        plants (list[Plant]): A list of plants in the garden.
    """
    def __init__(self) -> None:
        """Initialize a GardenManager instance."""
        self.plants: list[Plant] = []

    def adding_plant(self, name: str, water_level: int, sun: int) -> None:
        """Add a plant to the garden, raising errors for invalid names.
        Args:
            name (str): The name of the plant to add.
        Raises:
            PlantError: If the plant name is empty or not found in catalog.
        """
        if not name.strip():
            raise PlantError("Plant name cannot be empty!")
        new_plant = Plant(name, water_level, sun)
        self.plants.append(new_plant)
        print(f"Added {name} successfully")

    def watering_plants(self) -> None:
        """Water all plants in the garden, ensuring cleanup after watering.
        Raises:
            WaterError: If watering fails for any plant.
        """
        print("Watering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                plant.water_level += 1
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def checking_plants_health(self) -> None:
        """Check the health of all plants, raising errors for unhealthy plants.
        Raises:
            WaterError: If a plant's water level is too low or high.

        """
        print("Checking plant health...")
        for plant in self.plants:
            try:
                if plant.water_level > 10:
                    raise WaterError(
                        f"{plant.name}: Water level {plant.water_level} "
                        "is too high (max 10)")
                elif plant.water_level < 1:
                    raise WaterError(
                        f"Water level {plant.water_level} "
                        "is too low (min 1)")
                if (plant.sunlight_hours < 2):
                    raise GardenError(
                        f"Sunlight hours {plant.sunlight_hours} "
                        "is too low (min 2)")
                elif (plant.sunlight_hours > 12):
                    raise GardenError(
                        f"Sunlight hours {plant.sunlight_hours} "
                        "is too high (max 12)")
                print(
                    f"{plant.name}: healthy (water: {plant.water_level}, "
                    f"sun: {plant.sunlight_hours})")
            except GardenError as e:
                print(f"Error checking {e}\n")


def test_garden_management() -> None:
    """Test the Garden Management System with error handling."""
    print("=== Garden Management System ===\n")
    garden = GardenManager()

    print("Adding plants to garden...")
    plant_data = [("tomato", 4, 8), ("lettuce", 14, 8), ("", 5, 8)]
    for name, water_level, sun in plant_data:
        try:
            garden.adding_plant(name, water_level, sun)
        except PlantError as e:
            print(f"Error adding plant: {e}\n")

    garden.watering_plants()

    garden.checking_plants_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
