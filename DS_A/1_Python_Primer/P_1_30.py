from custom_typing import number


def times_divisible_by_two(num: number) -> int:
    """
    number of times a number can be repeatedly divided by 2 before getting a v-
    alue less than 2
    """
    if (num / 2) < 2:
        return 0

    return 1 + times_divisible_by_two(num / 2)


if __name__ == "__main__":
    num = float(input("number: "))
    times = times_divisible_by_two(num)
    print(times, "times", num, "can be repeatedly divided by 2")

assert times_divisible_by_two(4) == 1
assert times_divisible_by_two(8) == 2
assert times_divisible_by_two(10) == 2
