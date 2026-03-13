
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = round(total_power / len(mages), 2)
    return {
        'max_power': max(mages, key=lambda mage: mage['power'])['power'],
        'min_power': min(mages, key=lambda mage: mage['power'])['power'],
        'avg_power': avg_power
    }


def data_mage() -> None:
    mages = [{'name': 'Morgan', 'power': 56, 'element': 'shadow'},
             {'name': 'Alex', 'power': 62, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 51, 'element': 'shadow'},
             {'name': 'Kai', 'power': 92, 'element': 'shadow'},
             {'name': 'Morgan', 'power': 78, 'element': 'shadow'}]
    print("Testing data mage...")
    mages_filter = mage_stats(mages)
    print(mages_filter)


def data_spell() -> None:
    spells = ['flash', 'heal', 'tornado', 'blizzard']
    change_spell = spell_transformer(spells)
    print("Testing change spell...")
    print(change_spell)
    print()


def data_power() -> None:
    mages = [{'name': 'Morgan', 'power': 56, 'element': 'shadow'},
             {'name': 'Alex', 'power': 62, 'element': 'fire'},
             {'name': 'Phoenix', 'power': 51, 'element': 'shadow'},
             {'name': 'Kai', 'power': 92, 'element': 'shadow'},
             {'name': 'Morgan', 'power': 78, 'element': 'shadow'}]
    mages_filter = power_filter(mages, 80)
    print("Testing mages filter...")
    print(mages_filter)
    print()


def data_artifacts() -> None:
    artifacts = [{'name': 'Storm Crown', 'power': 119, 'type': 'focus'},
                 {'name': 'Storm Crown', 'power': 88, 'type': 'focus'},
                 {'name': 'Fire Staff', 'power': 91, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 100, 'type': 'focus'}]
    sort_artifacts = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(sort_artifacts)
    print()


def main() -> None:
    data_artifacts()
    data_power()
    data_spell()
    data_mage()


if __name__ == "__main__":
    main()
