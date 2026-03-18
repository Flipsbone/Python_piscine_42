#!/usr/bin/env python3

""" ft_ancient_text.py A simple data recovery script for an ancient text file.
This script attempts to read from a file named 'ancient_fragment.txt'
and prints its contents to the console.
It includes error handling for cases where the file may not be found.
"""


def main() -> None:
    """ Main function to read and display the ancient text file. """

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = None
    try:
        file = open("ancient_fragment.txt", "r")
        print(f"Accessing Storage Vault: {file.name}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(file.read())
    except FileNotFoundError:
        print("ERROR:Storage vault not found. Run data generator first.")
    finally:
        if file is not None:
            file.close()
            print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":

    main()
