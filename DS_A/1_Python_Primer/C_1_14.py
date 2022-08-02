from collections.abc import Iterable


def pair_whose_producto_is_odd(sequence: Iterable[int]) -> bool:
    """
    from a sequence of integer values determines if there is a distinct pair
    if numbers whose producto is odd
    """

    sequence = list(set(sequence))

    for i, first in enumerate(sequence):
        for second in sequence[i + 1 :]:
            product_is_odd = ((first * second) % 2) == 1
            if product_is_odd:
                return True

    return False


assert pair_whose_producto_is_odd([1, 2, 3]) == True
assert pair_whose_producto_is_odd([2, 4, 6]) == False
assert pair_whose_producto_is_odd([2, 3]) == False
assert pair_whose_producto_is_odd([2, 3, 4]) == False
