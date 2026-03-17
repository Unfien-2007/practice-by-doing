
import datetime

name: str = input("What is your name? ")
age: int = int(input("What is your age? "))
birth_year: int = datetime.date.today().year - age

print(f"Hello, {name}! You are {age} years old.")
print(f"You were born around the year {birth_year}.")