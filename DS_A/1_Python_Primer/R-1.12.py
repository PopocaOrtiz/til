from collections.abc import Iterable
from typing import Union
from random import randrange

number = Union[int, float]


def choice(sequence: Iterable[number]) -> number:
    """
    own implementation of the random.choice function using randrange
    """
    sequence = tuple(sequence)
    index = randrange(len(sequence))
    return sequence[index]


assert choice((1, 2, 3)) in (1, 2, 3)
assert choice((1, 2, 3, 4, 5)) in (1, 2, 3, 4, 5)

