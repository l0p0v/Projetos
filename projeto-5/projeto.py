# PYTHON 3 NUMBER GUESSING GAME

from random import randint

try:
    inferior_limit = int(input("Enter lower bound: "))
    superior_limit = int(input("Enter upper bound: "))

    if inferior_limit > superior_limit:
        raise ValueError("Put the values in the correct order.")
    number = randint(inferior_limit, superior_limit)
except ValueError as err:
    print(f"ValueError: {err}")
else:
    print("\n\tYou've only 7 chances to guess the integer!\n")
    attempts = 0

    while attempts < 7:
        try:
            guess = int(input("Guess a number: "))
            attempts += 1

            if guess > number:
                print("You guessed too high!")
            elif guess < number:
                print("You guessed too small!")
            else:
                print(f"Congratulations you did it in {attempts} try")
                break
        except ValueError as err:
            print(f"ValueError: {err}")
    else:
        print(f"\nThe number is {number}")
        print("Better luck next time!")
