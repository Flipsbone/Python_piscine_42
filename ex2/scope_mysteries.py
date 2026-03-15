def mage_counter() -> callable:
    call = 0

    def inner_mage_counter() -> int:
        nonlocal call
        call += 1
        return call
    return inner_mage_counter


def spell_accumulator(initial_power: int) -> callable:
    def inner_spell_accumulator(power_add: int) -> int:
        nonlocal initial_power
        initial_power += power_add
        return initial_power
    return inner_spell_accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def inner_enchantment_factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return inner_enchantment_factory


def memory_vault() -> dict[str, callable]:
    vault_storage = {}

    def store(key: str, value: callable) -> None:
        vault_storage[key] = value

    def recall(key: str):
        return vault_storage.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    result_mage = mage_counter()
    for i in range(1, 4):
        print(f"call {i} : {result_mage()}")
    print()

    result_accumulator = spell_accumulator(5)
    for i in range(1, 4):
        print(f"Power increased {result_accumulator(10)}")
    print()

    enchentment = enchantment_factory("Flaming")
    print(f"{enchentment("Sword")}")
    enchantment_2 = enchantment_factory("Frozen")
    print(f"{enchantment_2("Shield")}")
    print()

    my_vault = memory_vault()
    my_vault['store']("counter", mage_counter)
    result_counter = my_vault['recall']("counter")
    result2_mage = result_counter()
    for i in range(1, 4):
        print(f"vault call {i} : {result2_mage()}")


if __name__ == "__main__":
    main()
