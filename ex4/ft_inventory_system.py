#!/usr/bin/env python3
""" Inventory System: A script to manage a player's inventory
using dictionary operations."""
import sys


def is_space(c: str) -> bool:
    return (c == " " or c == "\t" or c == "\n")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        key = ""
        value_str = ""
        word = True
        for char in arg:
            if is_space(char):
                continue
            if char == ":":
                word = False
                continue
            if word is True:
                key = key + char
            else:
                value_str = value_str + char
            inventory.update({key: int(value_str)})
    print(f"{inventory}")
