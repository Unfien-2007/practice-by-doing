# random guess game
import random as rd

answer = rd.randint(1, 99)

won = False
while not won:
    try:
        guess = int(input("Input Guess (1-99): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < 1 or guess > 99:
        print(f"Your Guess {guess} should be 1-99")
    elif answer == guess:
        print(f"Your Guess {guess} is the right answer")
        won = True
    elif guess > answer:
        print(f"Your Guess {guess} is Lower")
    else:
        print(f"Your Guess {guess} is Higher")


