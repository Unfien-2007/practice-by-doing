"""
Week 3 – Number Guessing Game
-------------------------------
The computer picks a secret number; the player tries to guess it within a
limited number of attempts.  A score is calculated based on how quickly the
player guesses correctly.
"""

import random

MAX_ATTEMPTS = 7
LOW = 1
HIGH = 100


def pick_secret(low: int = LOW, high: int = HIGH) -> int:
    """Return a random integer in the inclusive range [low, high]."""
    return random.randint(low, high)


def calculate_score(attempts_used: int, max_attempts: int) -> int:
    """
    Award more points for fewer attempts.
    Score is 100 on the first guess and 0 when all attempts are used.
    """
    if max_attempts <= 1:
        return 100 if attempts_used <= 1 else 0
    return max(0, round(100 * (max_attempts - attempts_used) / (max_attempts - 1)))


def play_round(secret: int, max_attempts: int = MAX_ATTEMPTS) -> dict:
    """
    Run one round of the guessing game.

    Returns a dict with keys:
        won       – bool
        attempts  – int (number of guesses made)
        score     – int
    """
    print(
        f"\nI've picked a number between {LOW} and {HIGH}. "
        f"You have {max_attempts} attempts.\n"
    )

    for attempt in range(1, max_attempts + 1):
        while True:
            raw = input(f"Attempt {attempt}/{max_attempts} – Enter your guess: ").strip()
            if raw.lstrip("-").isdigit():
                guess = int(raw)
                break
            print("Please enter a whole number.")

        if guess < secret:
            print("Too low! Try higher.\n")
        elif guess > secret:
            print("Too high! Try lower.\n")
        else:
            score = calculate_score(attempt, max_attempts)
            print(f"🎉 Correct! You guessed it in {attempt} attempt(s).")
            print(f"Score: {score}\n")
            return {"won": True, "attempts": attempt, "score": score}

    print(f"Out of attempts! The number was {secret}.\n")
    return {"won": False, "attempts": max_attempts, "score": 0}


def main() -> None:
    print("=== Number Guessing Game ===")
    wins = 0
    losses = 0

    while True:
        secret = pick_secret()
        result = play_round(secret)

        if result["won"]:
            wins += 1
        else:
            losses += 1

        print(f"Stats – Wins: {wins}  Losses: {losses}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
