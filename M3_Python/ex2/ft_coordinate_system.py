#!/usr/bin/env python3
""" Game Coordinate System: A script to handle 3D coordinates
and calculate distances."""
import math


def calculate_dist(orign_point: tuple, position: tuple) -> float:
    """Calculate the Euclidean distance between two 3D points.
    Args:
        orign_point (tuple): The origin point (x, y, z).
        position (tuple): The target position (x, y, z).
        Returns:
            float: The Euclidean distance between the two points.
    """
    x1 = position[0]
    x2 = orign_point[0]

    y1 = position[1]
    y2 = orign_point[1]

    z1 = position[2]
    z2 = orign_point[2]

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return dist


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    position_1 = (10, 20, 5)
    origin_point = (0, 0, 0)
    dist = calculate_dist(origin_point, position_1)
    print(f"Position created: {position_1}")
    print(f"Distance between {origin_point} and {position_1}: {dist:.2f}\n")

    parsing_2 = "3,4,0"
    print(f'Parsing coordinates: "{parsing_2}"')
    part = parsing_2.split(',')
    position_2 = []
    for cordonnate in part:
        position_2.append(int(cordonnate))
    tuple_position_2 = tuple(position_2)
    print(f"Parsed position: {tuple_position_2}")
    dist = calculate_dist(origin_point, tuple_position_2)
    print(f"Distance between {origin_point} and {tuple_position_2}: "
          f"{dist:.1f}\n")

    parsing_3 = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{parsing_3}"')
    part = parsing_3.split(',')
    position_3 = []
    try:
        for cordonnate in part:
            position_3.append(int(cordonnate))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__},"
              f"Args: {e.args}\n")

    print("Unpacking demonstration:")
    X, Y, Z = tuple_position_2
    print("Player at x={}, y={}, z={}".format(*tuple_position_2))
    print(f"Coordinates: X={X}, Y={Y}, Z={Z}")
