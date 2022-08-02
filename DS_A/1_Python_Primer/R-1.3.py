from collections.abc import Iterable
from typing import Union

number = Union[int, float]

def minmax(data: Iterable[number]) -> tuple[number, number]:
    """ 
    from a sequence of numbers return the min and the max without using
    min and max functions
    """

    data = tuple(data)

    minn = data[0]
    maxn = data[0]
    
    for num in data:
        if num > maxn:
            maxn = num
        if num < minn:
            minn = num

    return minn, maxn
            
assert minmax([1, 2, 3]) == (1, 3)
assert minmax([1, 2, -1, 3, 200, 4]) == (-1, 200)

