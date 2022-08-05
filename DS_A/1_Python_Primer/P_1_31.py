from typing_extensions import TypedDict

bills_and_coins: dict[str, list[float]] = {
    "bills": [2000, 1000, 500, 200, 100, 50, 20],
    # "bills": [20, 50, 100, 200, 500, 1000, 2000],
    "coins": [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1],
    # "coins": [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50],
}

Change = TypedDict("Change", {"bills": dict[int, int], "coins": dict[float, int]})


def make_change(difference: float) -> Change:
    """
    calculates the change, amount of bills and coins that can be given for a
    certain amount of money(difference between the amount given and the amount
    charged)
    """

    change: Change = {
        "bills": {},
        "coins": {},
    }

    for kind in bills_and_coins:

        for value in bills_and_coins[kind]:

            if value > difference:  # this bill/coin can't be used
                continue

            amount = difference // value

            change[kind][value] = amount

            difference -= amount * value

    return change


assert make_change(7.5) == {"bills": {}, "coins": {5: 1, 2: 1, 0.5: 1}}

if __name__ == "__main__":
    charged = float(input("charged: "))
    given = float(input("given: "))
    print(make_change(given - charged))
