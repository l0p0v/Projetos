from random import choice

print("""Winner rules as follows:
Rock vs Paper -> Paper win
Scissor vs Rock -> Rock win
Paper vs Scissor -> Scissors win""")

computer_points = 0
user_points = 0

while True:
    try:
        user_choice = int(input("""\nEnter choice:
1. Rock
2. Paper
3. Scissor
User turn: """))

        if user_choice == 1:
            user_choice = "Rock"
        elif user_choice == 2:
            user_choice = "Paper"
        elif user_choice == 3:
            user_choice = "Scissor"
        else:
            raise ValueError("\033[31mChoose a valid option\033[m")

        computer = choice(("Rock", "Paper", "Scissor"))

        print(f"\nUser choice is: {user_choice}")
        print(f"Computer choice is: {computer}")

        if user_choice == "Rock" and computer == "Paper":
            print("Rock vs Paper => Paper wins")
            computer_points += 1
        elif user_choice == "Paper" and computer == "Rock":
            print("Paper vs Rock => Paper wins")
            user_points += 1

        elif user_choice == "Scissor" and computer == "Rock":
            print("Scissor vs Rock => Rock wins")
            computer_points += 1
        elif user_choice == "Rock" and computer == "Scissor":
            print("Rock vs Scissor => Rock wins")
            user_points += 1

        elif user_choice == "Paper" and computer == "Scissor":
            print("Paper vs Scissor => Scissor wins")
            computer_points += 1
        elif user_choice == "Scissor" and computer == "Paper":
            print("Scissor vs Paper => Scissor wins")
            user_points += 1

        else:
            print(f"{user_choice} vs {computer} => Draw")

        print(f"""\nScoreboard:
User: {user_points}
Computer: {computer_points}\n""")

    except ValueError as err:
        print(f"ValueError: \033[31m{err}\033[m")
    finally:
        while True:
            try:
                again = input("Do you want to play again (y/n)? ").lower()[0]

                if again == "y" or again == "n":
                    break
                else:
                    raise ValueError
            except (IndexError, ValueError):
                print(f"\033[31mEnter (y/n)\033[m")
        if again == "y":
            continue
        else:
            print()
            break

if user_points > computer_points:
    print("<== User wins ==>")
elif computer_points > user_points:
    print("<== Computer wins ==>")
else:
    print("<== Draw ==>")

print(f"User points: {user_points}")
print(f"Computer points: {computer_points}")
