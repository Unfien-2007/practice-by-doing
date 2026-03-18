
import datetime

name: str = input("What is your name? ")
age: int = int(input("What is your age? "))
birth_year: int = datetime.date.today().year - age
future_age: int = age + 10
fav_color: str = input("What is your favorite color? ")
months_old: int = age * 12

print(f"Hello, {name}! You are {age} years old.")
print(f"You were born around the year {birth_year}.")
print(f"In 10 years you will be {future_age} years old.")
print(f"Your favorite color is {fav_color}.")
