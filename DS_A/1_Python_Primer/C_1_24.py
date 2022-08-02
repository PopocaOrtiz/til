def count_vowels(word: str) -> int:
    """
    count vowels in a string
    """
    total = 0
    vowels = [letter for letter in word if letter in "aeiouAEIOU"]
    return len(vowels)


if __name__ == "__main__":
    assert count_vowels("hello") == 2
    assert count_vowels("{ell@") == 1
    assert count_vowels("123") == 0
