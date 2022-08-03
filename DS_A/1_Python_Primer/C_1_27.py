from typing import Generator


def factors(n: int) -> Generator[int, None, None]:
    """
    reimplementation of the function
    def factors(n): # generator that computes factors
        k=1
        while k k < n: # while k < sqrt(n)
            if n % k == 0:
                yield k
                yield n // k
            k += 1
        if k k == n: # special case if n is perfect square
            yield k

    so the factors are returned in incremental order
    """
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            # yield n // k
        k += 1

    if k * k == n:
        yield k

    k -= 1
    while k > 0:
        if n % k == 0:
            yield n // k
        k -= 1


assert list(factors(100)) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
