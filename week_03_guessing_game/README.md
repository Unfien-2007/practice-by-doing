# Week 3: Number Guessing Game

**Difficulty:** Beginner → Intermediate

## Learning Goals
- Use the `random` module
- Implement game loops with win/lose conditions
- Track state across iterations (attempts, score)
- Provide helpful feedback to the user

## Project Description
The computer picks a random integer between 1 and 100. The player has a limited
number of attempts to guess the number. After each guess the program tells the
player whether their guess is too high, too low, or correct. At the end the
player's score is displayed and they can play again.

## Concepts Covered
- `random.randint()`
- `while` loops with counters
- Comparison operators
- Accumulating state (attempts, wins, losses)
- Simple scoring

## How to Run
```bash
python main.py
```

## Sample Output
```
=== Number Guessing Game ===
I've picked a number between 1 and 100. You have 7 attempts.

Attempt 1/7 – Enter your guess: 50
Too high! Try lower.

Attempt 2/7 – Enter your guess: 25
Too low! Try higher.

Attempt 3/7 – Enter your guess: 37
🎉 Correct! You guessed it in 3 attempts.
Score: 80

Play again? (y/n):
```

## Challenges
1. Let the player choose the difficulty (easy=10 attempts, hard=5 attempts).
2. Add a leaderboard that persists across sessions using a file.
3. Allow the player to set the number range.
