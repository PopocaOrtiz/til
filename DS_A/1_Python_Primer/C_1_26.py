def can_be_used(a: int, b: int, c: int) -> bool:
    """
    determines if numbers form a correct arithmetic formula
    a + b = c
    a = b - c
    a * b = c
    """
    if (a + b) == c:
        return True
    if a == (b - c):
        return True
    if (a * b) == c:
        return True

    return False


assert can_be_used(1, 2, 3) == True
assert can_be_used(1, 2, 4) == False
assert can_be_used(2, 5, 3) == True
assert can_be_used(3, 5, 3) == False
assert can_be_used(2, 3, 6) == True
assert can_be_used(2, 3, 7) == False

if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    print(can_be_used(a, b, c))
