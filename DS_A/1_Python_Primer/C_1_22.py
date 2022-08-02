from collections.abc import Iterable
from typing import Generator


def dot_product(a: Iterable[int], b: Iterable[int]) -> Generator[int, None, None]:
    """
    returns the dot producto of a and b
    """
    a = tuple(a)
    b = tuple(b)
    for index, _ in enumerate(a):
        yield a[index] * b[index]


assert list(dot_product([1, 2], [1, 2])) == [1, 4]
assert list(dot_product([2, 4, 8], [3, 6, 9])) == [6, 24, 72]
