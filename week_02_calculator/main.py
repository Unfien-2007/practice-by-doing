"""
Week 2 – Simple Calculator
---------------------------
An interactive CLI calculator that supports +, -, *, and /.
The session continues until the user types 'q' to quit.
"""

SUPPORTED_OPS = {"+", "-", "*", "/"}


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate(a: float, op: str, b: float) -> float:
    """Dispatch to the correct arithmetic function based on *op*."""
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if op not in operations:
        raise ValueError(f"Unsupported operator: '{op}'. Use one of {SUPPORTED_OPS}.")
    return operations[op](a, b)


def get_number(prompt: str) -> float:
    """Prompt the user until a valid float is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_operator() -> str:
    """Prompt the user until a valid operator is entered."""
    while True:
        op = input(f"Choose operation ({', '.join(sorted(SUPPORTED_OPS))}): ").strip()
        if op in SUPPORTED_OPS:
            return op
        print(f"Invalid operator. Please choose from: {', '.join(sorted(SUPPORTED_OPS))}")


def main() -> None:
    print("=== Simple Calculator ===")
    while True:
        a = get_number("Enter first number: ")
        op = get_operator()
        b = get_number("Enter second number: ")

        try:
            result = calculate(a, op, b)
            print(f"Result: {a} {op} {b} = {result}\n")
        except ZeroDivisionError as exc:
            print(f"Error: {exc}\n")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
