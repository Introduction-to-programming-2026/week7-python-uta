# Project 2 — Number Guessing Game
# Author: Ulpiana

import random

# TODO: generate a random secret number between 1 and 10
secret_number = random.randint(1,10)
# TODO: set up a guesses counter
guesses_count = 0
# TODO: get the user's first guess
print("I'm thinking of a number between 1 and 10. Can you guess it?")
# TODO: while loop — keep asking until the guess is correct
#   - print "Too low!" or "Too high!" on each wrong guess
#   - count each guess
while True:
    try:
        guess = int(input("enter your guess "))
        guesses_count += 1  # count each guess

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            # The guess is correct!
            break

    except ValueError:
        print("Please enter a valid whole number.")
# TODO: print the congratulations message with the number of guesses
print(f"Congrats you had {guesses_count} guesses.")
