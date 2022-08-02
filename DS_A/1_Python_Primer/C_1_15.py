from collections.abc import Iterable
from custom_typing import number


def all_different(sequence: Iterable[number]) -> bool:
    """
    from a sequence of numbers determines if all of them are different
    """
    return list(sequence) != list(set(sequence))


assert all_different([1, 2, 3]) == False
assert all_different([1, 2, 1]) == True
