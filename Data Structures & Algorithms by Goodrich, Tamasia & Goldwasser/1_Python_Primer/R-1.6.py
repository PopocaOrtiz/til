def sum_of_squares_odd_smaller(n: int) -> int:
    """
    returns the sum of the squares of all the odd positive integers smaller 
    than n
    """
    return sum([num * num for num in range(n) if num % 2 == 1])

assert sum_of_squares_odd_smaller(2) == 1
assert sum_of_squares_odd_smaller(3) == 1
assert sum_of_squares_odd_smaller(4) == 10

