#!/usr/bin/env python3

import alchemy.grimoire


def ingredient_validation() -> None:
    print("Testing ingredient validation:")
    ingredients = "fire air"
    result = alchemy.grimoire.validate_ingredients(ingredients)
    print(f'validate_ingredients("{ingredients}"): {result}')
    ingredients = "dragon scales"
    result = alchemy.grimoire.validate_ingredients(ingredients)
    print(f'validate_ingredients("{ingredients}"): {result}')


def spell_validation() -> None:
    print("\nTesting spell recording with validation:")
    spell = "Fireball"
    ingredients = "fire air"
    result = alchemy.grimoire.record_spell(spell, ingredients)
    print(f'record_spell("{spell}", "{ingredients}"): {result}')

    spell = "Dark Magic"
    ingredients = "shadow"
    result = alchemy.grimoire.record_spell(spell, ingredients)
    print(f'record_spell("{spell}", "{ingredients}"): {result}')


def late_import_validation() -> None:
    print("\nTesting late import technique:")
    spell = "Lightning"
    ingredients = "air"
    result = alchemy.grimoire.record_spell(spell, ingredients)
    print(f'record_spell("{spell}", "{ingredients}"): {result}')


def main():
    print("=== Circular Curse Breaking ===")

    try:
        ingredient_validation()
        spell_validation()
        late_import_validation()
    except Exception as e:
        print(f"\nUNEXPECTED ERROR: {e}")

    print("\nAll spells processed safely!")


if __name__ == "__main__":
    main()
