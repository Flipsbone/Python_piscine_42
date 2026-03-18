#!/usr/bin/env python3
""" ft_archive_creation.py A simple data archiving script for a new discovery.
This script creates a file named 'new_discovery.txt'
and writes several entries into it.
It includes error handling for cases where the file cannot be created or
written to.
"""


def main() -> None:
    """ Main function to create and write to the archive file. """

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file = None
    try:
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data..")
        entry_1 = "[ENTRY 001] New quantum algorithm discovered.\n"
        entry_2 = "[ENTRY 002] Efficiency increased by 347%\n"
        entry_3 = "[ENTRY 003] Archived by Data Archivist trainee\n"

        file.write(entry_1)
        print(f"{entry_1.strip()}")
        file.write(entry_2)
        print(f"{entry_2.strip()}")
        file.write(entry_3)
        print(f"{entry_3}")

    except PermissionError:
        print("ERROR: Permission denied. Cannot write to storage vault.")
    finally:
        if file is not None:
            file.close()
            print("Data inscription complete. Storage unit sealed.")
            print(f"Archive {file.name} ready for long-term preservation.")


if __name__ == "__main__":

    main()
