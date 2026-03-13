def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            try:
                results.append(spell(*args, **kwargs))
            except Exception:
                results.append(None)
        return results
    return sequence


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        except Exception:
            return "Spell fizzled"
    return caster


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        try:
            return base_spell(*args, **kwargs) * multiplier
        except Exception:
            return None
    return amplified


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> tuple:
        try:
            return (spell1(*args, **kwargs), spell2(*args, **kwargs))
        except Exception:
            return None
    return combined


def light(mana: int) -> str:
    return f"light is use with {mana} mana"


def enough_mana(mana: int) -> bool:
    return mana >= 10


def basic_damage() -> int:
    return 10


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def test_sequence() -> None:
    print("Testing spell_sequence...")
    spell = [fireball, heal]
    combo = spell_sequence(spell)
    result = combo("target")
    print(result)
    print()


def conditional() -> None:
    print("Testing conditionnal caster...")
    cast_spell = conditional_caster(enough_mana, light)
    result = cast_spell(10)
    print(result)
    print()


def power() -> None:
    print("Testing power amplifier...")
    my_amplified_power = power_amplifier(basic_damage, 3)
    orignial = basic_damage()
    amplified_damage = my_amplified_power()
    print(f"original : {orignial} amplificateur : {amplified_damage}")
    print()


def spell() -> None:
    print("Testing spell combiner...")
    my_combined_spell = spell_combiner(fireball, heal)
    result = my_combined_spell("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()


def main() -> None:
    spell()
    power()
    conditional()
    test_sequence()


if __name__ == "__main__":
    main()
