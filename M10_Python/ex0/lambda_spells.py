def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(
            artifacts,
            key=lambda artifact: artifact['power'],
            reverse=True
            )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(filter(lambda mage: mage['power'] >= min_power, mages))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda spell: f"* {spell} *", spells))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def mage_stats(mages: list[dict]) -> dict:
    try:
        if not mages:
            return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
        total_power = sum(map(lambda mage: mage['power'], mages))
        avg_power = round(total_power / len(mages), 2)
        return {
            'max_power': max(mages, key=lambda mage: mage['power'])['power'],
            'min_power': min(mages, key=lambda mage: mage['power'])['power'],
            'avg_power': avg_power
        }
    except Exception:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}


def data_mage() -> None:
    print("Testing data mage...")
    mages = [{'name': 'Morgan', 'power': 56, 'element': 'shadow'},
             {'name': 'Alex', 'power': 62, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 51, 'element': 'shadow'},
             {'name': 'Kai', 'power': 92, 'element': 'shadow'},
             {'name': 'Morgan', 'power': 78, 'element': 'shadow'}]
    mages_filter = mage_stats(mages)
    print(mages_filter)


def data_spell() -> None:
    print("Testing change spell...")
    spells = ['flash', 'heal', 'tornado', 'blizzard']
    change_spell = spell_transformer(spells)
    print(change_spell)
    print()


def data_power() -> None:
    print("Testing mages filter...")
    mages = [{'name': 'Morgan', 'power': 56, 'element': 'shadow'},
             {'name': 'Alex', 'power': 62, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 51, 'element': 'shadow'},
             {'name': 'Kai', 'power': 92, 'element': 'shadow'},
             {'name': 'Morgan', 'power': 78, 'element': 'shadow'}]
    mages_filter = power_filter(mages, 80)
    print(mages_filter)
    print()


def data_artifacts() -> None:
    print("Testing artifact sorter...")
    artifacts = [{'name': 'Storm Crown', 'power': 119, 'type': 'focus'},
                 {'name': 'Storm Crown', 'power': 88, 'type': 'focus'},
                 {'name': 'Fire Staff', 'power': 91, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 100, 'type': 'focus'}]
    sort_artifacts = artifact_sorter(artifacts)
    print(f"{sort_artifacts[0]['name']} ({sort_artifacts[0]['power']} power) "
          "comes before "
          f"{sort_artifacts[1]['name']} ({sort_artifacts[1]['power']} power)"
          )
    print()


def main() -> None:
    data_artifacts()
    data_power()
    data_spell()
    data_mage()


if __name__ == "__main__":
    main()
