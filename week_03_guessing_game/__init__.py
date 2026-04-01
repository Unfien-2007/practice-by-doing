#random guese game

import random as rd

guess = int(input("Input Guess(1-99): "))

#logic 

answer = rd.randrange(1,99)

if answer == guess :
    print(f"Your Guess {guess} is the right answer")


