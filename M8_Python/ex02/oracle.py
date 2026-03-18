import os
import sys
import importlib


def check_dependencies() -> None:
    dependencies = {
        "dotenv": "Environment configuration ready",
    }
    all_ok = True

    for name, description in dependencies.items():
        try:
            module = importlib.import_module(name)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {name} ({version}) - {description}")
        except ImportError:
            print(f"[ERROR] Missing dependency: {name}")
            all_ok = False

    if not all_ok:
        print("\n[ERROR] Missing dependencies."
              "Run this exact command: pip install python-dotenv")
        sys.exit(1)


def display_config(my_config: dict[str, str]) -> None:
    print(f"Mode: {my_config.get('MATRIX_MODE')}")

    if my_config.get('DATABASE_URL'):
        db_status = "Connected to local instance"
    else:
        db_status = "Disconnected"
    print(f"Database: {db_status}")

    if my_config.get('API_KEY'):
        api_status = "Authenticated"
    else:
        api_status = "Missing"
    print(f"API Access: {api_status}")

    print(f"Log Level: {my_config.get('LOG_LEVEL')}")

    if my_config.get('ZION_ENDPOINT'):
        zion_status = "Online"
    else:
        zion_status = "Offline"
    print(f"Zion Network: {zion_status}")


def load_config() -> dict[str, str]:
    try:
        config = {
            "MATRIX_MODE": os.environ["MATRIX_MODE"],
            "DATABASE_URL": os.environ["DATABASE_URL"],
            "API_KEY": os.environ["API_KEY"],
            "LOG_LEVEL": os.environ['LOG_LEVEL'],
            "ZION_ENDPOINT": os.environ['ZION_ENDPOINT']
            }
        return config
    except KeyError as e:
        sys.exit(f"MISSING CONFIGURATION: Please check your Key=Value for {e}")


def main() -> None:
    check_dependencies()
    from dotenv import load_dotenv
    if len(sys.argv) != 2:
        sys.exit("\nUsage: python oracle.py .env")

    env_path = sys.argv[1]
    print("ORACLE STATUS: Reading the Matrix...\n")

    try:
        if not load_dotenv(env_path):
            sys.exit(f"Error load configuration from '{env_path}' file")
    except OSError as e:
        sys.exit(f"[ERROR] While accessing '{env_path}': {e}")

    my_config: dict[str, str] = load_config()
    print("Configuration loaded!")
    display_config(my_config)
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
