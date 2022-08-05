from typing import Sequence


def all_possible_strings(letters: Sequence[str]) -> Sequence[str]:
    """
    all possible strings formed by using the characters exactly once
    """

    # base case
    if len(letters) == 2:
        return [
            letters[0] + letters[1],
            letters[1] + letters[0],
        ]

    all_combinations: list[str] = []
    for index, letter in enumerate(letters):
        sublist = list(letters)
        sublist.pop(index)

        subcombinations = all_possible_strings(sublist)
        for subcombination in subcombinations:
            all_combinations.append(letter + subcombination)

    return all_combinations


assert all_possible_strings("ab") == ["ab", "ba"]
assert all_possible_strings("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]

if __name__ == "__main__":
    print(all_possible_strings("catdog"))
