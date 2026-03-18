from .spellbook import record_spell
__all__ = ['record_spell']


def validate_ingredients(ingredients: str) -> str:
    if not isinstance(ingredients, str):
        raise TypeError("Ingredients must be a string")

    try:
        valid_elements = {"fire", "water", "earth", "air"}
        list_ingredients = ingredients.split()
        for ingredient in list_ingredients:
            if ingredient not in valid_elements:
                return f"{ingredients} - INVALID"
        return f"{ingredients} - VALID"

    except (AttributeError, TypeError) as e:
        return f"Error: Invalid input format. {e}"
