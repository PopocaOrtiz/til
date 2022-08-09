from typing import Literal


class Calculator:

    total: float = 0
    prev_operator: Literal["+", "-", None] = None

    def operate(self, operator: str) -> float:
        """
        receives a number or an operator and calculate the result
        if its a number it needs a previously saved operator
        """
        if operator == "+":
            self.prev_operator = "+"
            return self.total

        if operator == "-":
            self.prev_operator = "-"
            return self.total

        if not self.prev_operator:
            # previously there must be an operator to operate with
            raise Exception("operation is not defined")

        try:
            operand = float(operator)
        except ValueError:
            raise ValueError("input is not a number or an operator")

        self.total += +operand if self.prev_operator == "+" else -operand
        self.prev_operator = None

        return self.total


calculator = Calculator()
calculator.operate("+")
assert calculator.operate("3") == 3
calculator.operate("-")
assert calculator.operate("2") == 1


if __name__ == "__main__":

    calculator = Calculator()
    print("total:", 0)
    while True:
        operator = input("input: ")
        result = calculator.operate(operator)
        print("total:", result)
