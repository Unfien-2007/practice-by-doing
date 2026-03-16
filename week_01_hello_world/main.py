"""
Week 1 – Hello World & Basic I/O
---------------------------------
A simple greeting program that collects the user's name and age,
then displays personalised information.
"""

import datetime


def get_name() -> str:
    """Prompt the user for their name and return it."""
    return input("What is your name? ").strip()


def get_age() -> int:
    """Prompt the user for their age, validate it, and return it as an int."""
    while True:
        raw = input("How old are you? ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a valid positive whole number for your age.")


def calculate_birth_year(age: int) -> int:
    """Return the approximate birth year based on the current year and age."""
    current_year = datetime.date.today().year
    return current_year - age


def greet(name: str, age: int) -> None:
    """Print a personalised greeting with some fun facts."""
    birth_year = calculate_birth_year(age)
    months_old = age * 12
    future_age = age + 10

    print(f"\nHello, {name}! You are {age} years old.")
    print(f"You were born around the year {birth_year}.")
    print(f"That means you are approximately {months_old} months old.")
    print(f"In 10 years you will be {future_age} years old.")


def main() -> None:
    name = get_name()
    age = get_age()
    greet(name, age)


if __name__ == "__main__":
    main()
