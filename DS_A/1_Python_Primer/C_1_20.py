from typing import Generator, Iterable
from random import randint

from custom_typing import number


def custom_shuffle_v1(sequence: Iterable[int]) -> Generator[int, None, None]:
    """
    custom random.suffle function using random.randint function
    v1
    """

    sequence = list(sequence)

    for _ in range(len(sequence)):
        index = randint(0, len(sequence) - 1)
        yield sequence[index]
        sequence.pop(index)


def custom_shuffle_v2(sequence: Iterable[number]) -> list[number]:
    """
    custom random.shuffle function using random.randint function
    v2
    """

    sequence = list(sequence)
    for current, _ in enumerate(sequence):
        new = randint(0, len(sequence) - 1)
        sequence[current], sequence[new] = sequence[new], sequence[current]

    return sequence


assert set(custom_shuffle_v2([1, 2, 3])) == {1, 2, 3}
