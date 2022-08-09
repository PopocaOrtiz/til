class Calculator:
    total: float = 0

    def clear(self) -> None:
        self.total = 0

    def operate(self, operator: str, number: float) -> None:
        if operator == "+":
            self.total += number
        if operator == "-":
            self.total -= number
        if operator == "*":
            self.total *= number
        if operator == "/":
            self.total /= number

    def parse(self, operation: str) -> None:
        """
        iterates over each character, resolving operators(even when multiple)
        then apply the operation
        """

        operators = ["+", "-", "*", "/"]

        parsed = ""
        prev_operator = None
        prev_number = ""
        for char in operation:

            operators = ["+", "-", "*", "/"]

            if char not in operators and not prev_operator:
                raise Exception("stntaxis error")

            if char not in operators:
                prev_number += char
                continue

            if prev_number and prev_operator:
                number = float(prev_number)
                self.operate(prev_operator, number)
                prev_number = ""
                prev_operator = None

            if char == "+" and prev_operator in ["+", "-"]:
                continue
            if char == "-" and prev_operator in ["+", "-"]:
                prev_operator = "-" if prev_operator == "+" else "-"
                continue
            if char in operators and prev_operator:
                raise Exception("syntaxis error")
            if char in operators:
                prev_operator = char
                continue

        if prev_number and prev_operator:
            number = float(prev_number)
            self.operate(prev_operator, number)

        if prev_operator and not prev_number:
            raise Exception("syntaxis error")


calculator = Calculator()
calculator.parse("+1")
assert calculator.total == 1.0
calculator.parse("*3")
assert calculator.total == 3.0
calculator.parse("-2")
assert calculator.total == 1.0
calculator.parse("/1")
assert calculator.total == 1.0

if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print("c - clear")
        print("e - exit")
        operation = input(str(calculator.total) + ": ")

        if operation == "c":
            calculator.clear()
            continue

        if operation == "e":
            quit()

        calculator.parse(operation)
