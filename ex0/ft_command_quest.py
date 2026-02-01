#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")

    print(f"Program name: {sys.argv[0]}")

    if len(sys.argv) > 1:
        nb_args = len(sys.argv) - 1
        i = 1
        print(f"Arguments received: {nb_args}")
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")
