def is_even(k: int) -> bool:
    even = True
    for i in range(k):
       even = not even 
    return even

assert is_even(2) == True
assert is_even(3) == False
assert is_even(8474) == True
assert is_even(846481) == False

