#!/usr/bin/env python3
""" Inventory System: A script to manage a player's inventory
using dictionary operations."""
import sys


def display_dictionary(inventory: dict) -> None:
    """ Demonstrates dictionary properties.
    Args:
        inventory (dict): The inventory dictionary.
    """
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory} ")


def management_suggestion(inventory: dict) -> None:
    """ Suggests items that need restocking.
    Args:
        inventory (dict): The inventory dictionary.
    """
    restock = []
    for item, qty in inventory.items():
        if qty < 2:
            restock.append(item)
    print(f"Restock needed: {restock}")


def rarity_item(inventory: dict) -> None:
    """ Categorizes items based on their quantity.
    Args:
        inventory (dict): The inventory dictionary.
    """
    categories = {
        "Moderate": {},
        "Scarce": {},
    }
    for item, qty in inventory.items():
        if qty > 3:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")


def display_inventory(inventory: dict, total_item: int) -> None:
    """ Displays the inventory sorted by quantity.
    Args:
        inventory (dict): The inventory dictionary.
        total_item (int): Total number of items.
    """
    temp_inventory = inventory.copy()
    while temp_inventory:
        current_max = max(temp_inventory, key=temp_inventory.get)
        value = temp_inventory[current_max]
        try:
            inventory_share = ((value / total_item)) * 100
            print(f"{current_max}: {value} units {inventory_share:.1f}%")
        except ZeroDivisionError as e:
            print(f"Error : total_item {e}")
        del temp_inventory[current_max]
    print("\n=== Inventory Statistics ===")
    top_item = max(inventory, key=inventory.get)
    low_item = min(inventory, key=inventory.get)
    print(f"Most abundant: {top_item} ({inventory[top_item]} units)")
    print(f"Least abundant: {low_item} ({inventory[low_item]} units)")


def count_total_item(inventory: dict) -> int:
    """ Counts the total number of items in the inventory.
    Args:
        inventory (dict): The inventory dictionary.
    Returns:
        int: Total number of items.
    """
    return sum(inventory.values())


def fill_out_inventory(inventory: dict) -> dict:
    """ Fills out the inventory from command-line arguments.
    Args:
        inventory (dict): The inventory dictionary.
    Returns:
        dict: Updated inventory dictionary.
    """
    for arg in sys.argv[1:]:
        key = ""
        value_str = ""
        parse = arg.split(":", 1)
        if len(parse) == 2:
            key = parse[0].strip().lower()
            value_str = parse[1].strip()
            try:
                value_int = int(value_str)
                current_val = inventory.get(key, 0)
                value_int = current_val + value_int
                inventory.update({key: value_int})
            except ValueError:
                print(f"Skipping invalid quantity must be a number:"
                      f"'{value_str}' for item '{key}'")
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("No item provided. Usage: python3 ft_inventory_system.py "
              "<item:number> <sword:1> ...")

    if (len(sys.argv)) > 1:

        inventory = {}

        fill_out_inventory(inventory)

        nb_unique_item = len(inventory)
        total_item = count_total_item(inventory)

        print(f"Total items in inventory: {total_item}")
        print(f"Unique item types: {nb_unique_item}")

        if total_item > 0:
            print("\n=== Current Inventory ===")
            display_inventory(inventory, total_item)
            print("\n=== Item Categories ===")
            rarity_item(inventory)
            print("\n=== Management Suggestions ===")
            management_suggestion(inventory)
            print("\n=== Dictionary Properties Demo ===")
            display_dictionary(inventory)
