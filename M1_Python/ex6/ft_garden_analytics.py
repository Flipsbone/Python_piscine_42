#!/usr/bin/env python3
"""Module defining plant classes and garden management system."""


class Plant:
    """
    Blueprint for a plant that can grow and age.
    Attributes:
        name (str): The species name of the plant.
        height (int): The height in centimeters.
        growth (int): The growth rate in centimeters per day.
    """
    def __init__(self, name: str, height: int = 0, growth: int = 0) -> None:
        """Initialize plant and set initial values through secure methods.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            growth (int): The growth rate in centimeters per day.
        """
        self.name = name.capitalize()
        self.__height: int = 0
        self.__age: int = 0
        self.set_height(height)
        self.set_growth(growth)

    def set_height(self, height: int) -> None:
        """Validate and set height if non-negative.
        Args:
            height (int): The height in centimeters.
        """
        if height >= 0:
            self.__height = height

    def get_height(self) -> int:
        """Return the protected height."""
        return self.__height

    def set_growth(self, growth: int) -> None:
        """Validate and set growth if non-negative.
        Args:
            growth (int): The growth rate in centimeters per day.
        """
        if growth >= 0:
            self.__growth = growth

    def get_growth(self) -> int:
        """Return the protected growth."""
        return self.__growth


class FloweringPlant (Plant):
    """
    Specialized plant type that can bloom and has a color.
    Attributes:
        color (str): The color of the plant.
        Inherited attributes (name,height,growth)
        are managed by the Plant class.
    """
    def __init__(
            self, name: str, height: int, growth: int, color: str) -> None:
        """Initialize flowering plant with color.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            growth (int): The growth rate in centimeters per day.
            color (str): The color of the plant.
        """
        super().__init__(name, height, growth)
        self.color = color


class PrizeFlower (FloweringPlant):
    """
    Specialized flowering plant that can win prizes.
    Attributes:
        prize_point (int): The prize points awarded for this flower.
        Inherited attributes (name,height,growth,color)
        are managed by the FloweringPlant class.
    """
    def __init__(
            self, name: str, height: int,
            growth: int, color: str, prize_point: int):
        """Initialize prize flower with prize points.
        Args:
            name (str): The species name of the plant.
            height (int): The height in centimeters.
            growth (int): The growth rate in centimeters per day.
            color (str): The color of the plant.
            prize_point (int): The prize points awarded for this flower.
        """
        super().__init__(name, height, growth, color)
        self.prize_point = prize_point


class GardenManager:
    """
    Manages multiple gardens and their plants.
    Attributes:
        nb_gardens (int): Class variable tracking number of gardens.
        gardens (dict): A dictionary mapping garden names to lists of plants.
        name (str): The name of the garden manager.
        stats (GardenStats): An instance to track garden statistics.
    """
    nb_gardens = 0

    def __init__(self, name: str) -> None:
        """Initialize garden manager with a name.
        Args:
            name (str): The name of the garden manager.
            """
        self.gardens: dict[str, list[Plant]] = {}
        self.name = name
        self.stats = self.GardenStats()
        GardenManager.nb_gardens += 1

    class GardenStats:
        """
        Tracks statistics across all gardens.
        Attributes:
            count (int): Total number of plants added.
            total_growth (int): Cumulative growth of all plants.
            plant_type (dict): Counts of different plant types.
        """
        def __init__(self) -> None:
            """Initialize garden statistics."""
            self.count = 0
            self.total_growth = 0
            self.plant_type = {"Regular": 0, "Flowering": 0, "Prize": 0}

        def update(self, plant: Plant) -> None:
            """
            Update statistics with a new plant.
            Args:
                plant (Plant): The plant to add to statistics.
            """
            self.count += 1
            self.total_growth += plant.get_growth()
            if isinstance(plant, PrizeFlower):
                self.plant_type["Prize"] += 1
            elif isinstance(plant, FloweringPlant):
                self.plant_type["Flowering"] += 1
            else:
                self.plant_type["Regular"] += 1

        def display(self) -> None:
            """Display the collected garden statistics."""
            print(
                f"\nPlants added: {self.count}, "
                f"Total growth: {self.total_growth}cm")
            print(
                f"Plant types: {self.plant_type['Regular']} regular, "
                f"{self.plant_type['Flowering']} flowering, "
                f"{self.plant_type['Prize']} prize flowers\n")

    def add_plant(self, garden_name: str, plants: Plant) -> None:
        """Add a plant to a garden
            Args:
            garden_name (str): The name of the garden.
            plants (Plant): The plant object to add.
        """
        if garden_name not in self.gardens:
            self.gardens[garden_name] = []
        self.gardens[garden_name].append(plants)
        if garden_name == "Alice":
            print(f"Added {plants.name} to {garden_name}'s garden")
        self.stats.update(plants)

    def display_garden(self, garden_name: str) -> None:
        """Display the contents of a specific garden.
            Args:
                garden_name (str): The name of the garden.
        """
        if garden_name not in self.gardens:
            print("Garden name not found")
        else:
            print(f"\n=== {garden_name}'s Garden Report ===")
            print(f"Plants in {self.name}")
            for plant in self.gardens[garden_name]:
                info = f"- {plant.name}: {plant.get_height()}cm"
                if isinstance(plant, FloweringPlant):
                    info += f", {plant.color} flowers (blooming)"
                if isinstance(plant, PrizeFlower):
                    info += f", Prize points: {plant.prize_point}"
                print(info)

    def calculate_garden_score(self, garden_name: str) -> int:
        """Calculate the total score for a specific garden.
            Args:
                garden_name (str): The name of the garden.
                Returns:
                    int: The total score of the garden.
        """
        total_score = 0
        if garden_name in self.gardens:
            for plant in self.gardens[garden_name]:
                total_score += plant.get_height()
                if isinstance(plant, PrizeFlower):
                    total_score += plant.prize_point * 4
        return total_score

    def simulate_growth(plant_list: list[Plant], garden_name: str) -> None:
        """
        Simulate growth for all plants in a garden.
            Args:
                plant_list (list): List of plants in the garden.
                garden_name (str): Name of the garden.
            """
        print(f"\n{garden_name} is helping all plants grow...")
        for plant in plant_list:
            new_height = plant.get_height() + plant.get_growth()
            plant.set_height(new_height)
            print(f"{plant.name} grew {plant.get_growth()}cm")
    simulate_growth = staticmethod(simulate_growth)

    def create_garden_network(cls: type['GardenManager']) -> 'GardenManager':
        """
        Create a new garden manager with a default garden.
        Returns:
            GardenManager: A new instance of GardenManager with default garden.
        """
        new_manager = cls("Global Garden Network")
        new_manager.gardens["North"] = []
        return new_manager
    create_garden_network = classmethod(create_garden_network)


def show_manager_status(manager: GardenManager) -> None:
    """
    Display a summary of the gardens managed by a GardenManager instance.
        Args:
            manager (GardenManager): An instance of the GardenManager class.
    """
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    garden_1 = GardenManager("garden")
    oak = Plant("Oak Tree", 100, 1)
    rose = FloweringPlant("Rose", 25, 1, "red")
    sunflower = PrizeFlower("Sunflower", 50, 1, "yellow", 10)

    garden_1.add_plant("Alice", oak)
    garden_1.add_plant("Alice", rose)
    garden_1.add_plant("Alice", sunflower)
    GardenManager.simulate_growth(garden_1.gardens["Alice"], "Alice")
    garden_1.display_garden("Alice")
    garden_1.stats.display()

    test_plant = Plant("Test", 10, 1)
    test_plant.set_height(-5)
    print(f"Height validation test: {test_plant.get_height() == 10}")

    bobs_plant = Plant("bush", 92, 0)
    garden_1.add_plant("Bob", bobs_plant)
    score_alice = garden_1.calculate_garden_score("Alice")
    score_bob = garden_1.calculate_garden_score("Bob")
    print(f"Garden scores - Alice: {score_alice}, Bob: {score_bob}")
    show_manager_status(garden_1)
