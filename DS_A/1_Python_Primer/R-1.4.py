def sum_of_squares(n: int) -> int:
    """
    returns the sum of que squares of all positive integer smaller than n
    """
    return sum([smaller * smaller for smaller in range(n)])
        
assert sum_of_squares(1) == 0
assert sum_of_squares(2) == 1
assert sum_of_squares(5) == 30

