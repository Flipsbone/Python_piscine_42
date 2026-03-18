#!/usr/bin/env python3
""" ft_vault_security.py A secure vault access and preservation script.
This script reads from a classified data file and writes new security
protocols to another file.
It ensures secure handling of sensitive information.
"""


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(file.read())
            print()
        with open("security_protocols.txt", "w") as file_w:
            print("SECURE PRESERVATION:")
            entry_1 = "[CLASSIFIED] New security protocols archived\n"
            file_w.write(entry_1)
            print(f"{entry_1.strip()}")
            print("Vault automatically sealed upon completion\n")
    except PermissionError as e:
        print(f"ERROR: {e}.")
    except FileNotFoundError as e:
        print(f"ERROR: {e} not found.")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly: {e}")
    finally:
        print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
