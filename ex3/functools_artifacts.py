import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations_dict = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
        }
    if not spells:
        raise ValueError("The spell list cannot be empty.")
    try:
        op_func = operations_dict[operation]
        return functools.reduce(op_func, spells)
    except KeyError:
        raise ValueError(f"Unknown operation: {operation}")
    except TypeError:
        raise TypeError("The spell list must contain only numbers.")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return ({
        "fire_enchant": functools.partial(
            base_enchantment, 50, "Fire"),
        "ice_enchant": functools.partial(
            base_enchantment, 50, "Ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, 50, "Lightning")
    })


def simple_enchant(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {element} (Power: {power})"


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"Fibonacci param `{n}` must be an integer.")
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    def base_dispatcher(spell):
        return f"Unknown spell type: {type(spell).__name__}"
    dispatcher = functools.singledispatch(base_dispatcher)

    def int_spell(damage):
        return f"Casting Damage Spell: {damage} HP dealt!"

    def str_spell(enchantment):
        return f"Applying Enchantment: {enchantment}!"

    def list_spell(multi_cast):
        return f"Multi-casting {len(multi_cast)} spells: {', '.join(map(str, multi_cast))}"

    dispatcher.register(int, int_spell)
    dispatcher.register(str, str_spell)
    dispatcher.register(list, list_spell)

    return dispatcher


def main() -> None:
    try:
        print("Testing spell reducer...")
        print(spell_reducer([1, 2, 3, 4], "max"))
        print()

        print("Testing Partial Enchanter...")
        enchanter = partial_enchanter(simple_enchant)
        print(enchanter["ice_enchant"]("Wooden Shield"))
        print()

        print("Testing memoized fibonacci...")
        print(memoized_fibonacci(100))
        print(memoized_fibonacci.cache_info())
        print()

        print("Testing Spell Dispatcher...")
        dispatch = spell_dispatcher()
        print(dispatch(42))
        print(dispatch("Lightning"))
        print(dispatch(["Mud", "Fire", "Ice"]))
        print(dispatch(3.14))
    except (ValueError, TypeError) as e:
        print({e})


if __name__ == "__main__":
    main()