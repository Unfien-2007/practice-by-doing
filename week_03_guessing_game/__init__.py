#random guese game
import random as rd
answer = rd.randrange(1,99)

#logic 
if answer == guess :
        print(f"Your Guess {guess} is the right answer")
elif answer <= guess:
        print(f"Your Guess {guess} is Lower")
    elif answer >= guess & answer < 100:
        print(f"Your Guess {guess} is higher")
    else:
        print(f"Your Guess {guess} should be 1-99")


while answer != guess:
guess = int(input("Input Guess(1-99): "))

    


#error to fix program ran infinite


