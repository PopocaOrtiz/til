def remove_punctuation(word: str) -> str:
    """
    remove symbols of punctuation
    !,.'
    """
    for symbol in ["!", ",", ".", "'"]:
        word = word.replace(symbol, "")

    return word


if __name__ == "__main__":
    assert remove_punctuation("Let's try, Mike.") == "Lets try Mike"
