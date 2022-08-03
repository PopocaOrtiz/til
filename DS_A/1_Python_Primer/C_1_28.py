from typing import Sequence

from custom_typing import number


def norm(vector: Sequence[number], p: int = 2) -> number:
    """
    returns the p-norm of the vector, if p is omited it returns the Euclidean
    norm, i.e. p=2
    """
    total_sum = sum([num**p for num in vector])

    return total_sum ** (1 / p)


assert norm([4, 3]) == 5
assert round(norm([1, 2, 3]), 2) == 3.74
