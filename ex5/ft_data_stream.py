#!/usr/bin/env python3
""" Game Data Stream Processor: A script to process a stream of game events
using generator functions."""

import time
from typing import Generator


def generator(limit: int) -> Generator[list, None, None]:
    """ Simulates a stream of game event data.
    Args:
        limit (int): Number of events to generate.
    Yields:
        list: A list containing event data.
    """
    names = ["alice", "bob", "charlie"]
    lvl_starting = [5, 12, 7]
    kill_counts = [0, 0, 0]
    actions = ["killed monster", "found treasure", "leveled up"]
    lvl_event = 0
    treasure_event = 0

    for event in range(1, limit + 1):
        idx = (event - 1) % 3
        name = names[idx]
        action = actions[(event + (event // 3)) % len(actions)]
        if action == "killed monster":
            kill_counts[idx] += 1
        elif action == "leveled up":
            lvl_event += 1
            lvl_starting[idx] += 1
        elif action == "found treasure":
            treasure_event += 1
        yield [
            event,
            name,
            lvl_starting[idx],
            action,
            lvl_event,
            treasure_event
            ]


def handle_data(data: list, hight_count: int) -> int:
    """ Processes a single data entry from the stream.
    Args:
        data (list): The event data.
        hight_count (int): Current count of high-level players.
    Returns:
        int: Updated count of high-level players.
    """
    event, name, lvl, action, _, _ = data
    if lvl >= 10:
        hight_count += 1
    if event <= 3:
        print(f"Event {event}: Player {name} (level {lvl}) {action}")
    return hight_count


def run_analytics(event: int) -> None:
    """ Runs the analytics on the game data stream.
    Args:
        event (int): Number of events to process.
    """
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {event} game events...\n")

    start_time = time.perf_counter()
    hight_count = 0
    stream = iter(generator(event))
    try:
        first_data = next(stream)
        hight_count = handle_data(first_data, hight_count)
        last_data = [first_data[0], first_data[4], first_data[5]]

        for data in stream:
            event, name, lvl, action, lvl_event, treasure_event = data
            hight_count = handle_data(data, hight_count)
            last_data = [event, lvl_event, treasure_event]

    except StopIteration:
        last_data = None

    end_time = time.perf_counter()
    duration = end_time - start_time

    if last_data:
        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {event}")
        print(f"High-level players (10+): {hight_count}")
        print(f"Treasure events: {treasure_event}")
        print(f"Level-up events: {lvl_event}")
        print("\nMemory usage: Constant (streaming)")
        print(f"Processing time: {duration:.3f} seconds")


if __name__ == "__main__":
    run_analytics(1000)
