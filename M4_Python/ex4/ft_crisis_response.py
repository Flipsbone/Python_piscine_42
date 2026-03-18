#!/usr/bin/env python3
''' ft_crisis_response.py A crisis response simulation for archive access.
This script simulates various scenarios of archive access, including
successful retrieval, missing archives, and permission issues.
It demonstrates robust error handling to ensure system stability during crises.
'''


def access_archive(file_path: str, status: str) -> None:
    """ Simulates accessing an archive with error handling for many scenarios.
    Args:
        file_path (str): The path to the archive file to access.
        status (str): The status of access attempt).
    """
    print(f"{status}: Attempting access to '{file_path}'...")
    try:
        with open(file_path, 'r') as file:
            print(f"SUCCESS: Archive recovered - {file.read()}", end="")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly: {e}\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    access_archive("lost_archive.txt", "CRISIS ALERT")
    access_archive("classified_vault.txt", "CRISIS ALERT")
    access_archive("standard_archive.txt", "ROUTINE ACCESS")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
