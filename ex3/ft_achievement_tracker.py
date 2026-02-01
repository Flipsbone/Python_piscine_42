#!/usr/bin/env python3
""" Achievement Tracker System: A script to track player achievements
and analyze them using set operations."""

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}

    data_bob = ["first_kill", "level_10", "boss_slayer", "collector"]
    bob = set(data_bob)

    charlie = set()
    charlie.update(["level_10", "treasure_hunter", "boss_slayer",
                    "speed_demon", "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")
    unique_achievement = alice.union(bob, charlie)

    print(f"All unique achievements: {unique_achievement}")
    total_achivement = len(unique_achievement)
    print(f"Total unique achievements: {total_achivement}\n")

    common_all = alice.intersection(bob, charlie)
    print(f"Common to all players: {common_all}")

    only_alice = alice.difference(bob, charlie)
    only_bob = bob.difference(alice, charlie)
    only_charlie = charlie.difference(alice, bob)

    rare = only_alice.union(only_bob, only_charlie)
    print(f"Rare achievements (1 player): {rare}\n")

    common_alice_bob = alice.intersection(bob)
    print(f"Alice vs Bob common: {common_alice_bob}")

    only_alice_vs_bob = alice.difference(bob)
    print(f"Alice unique: {only_alice_vs_bob}")

    only_bob_vs_alice = bob.difference(alice)
    print(f"Bob unique: {only_bob_vs_alice}")
