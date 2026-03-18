def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    try:
        validate_result = validate_ingredients(ingredients)
        if "INVALID" in validate_result:
            return f"Spell rejected: {spell_name} ({validate_result})"
        else:
            return f"Spell recorded: {spell_name} ({validate_result})"
    except Exception as e:
        return f"Error processing spell '{spell_name}': {e}"
