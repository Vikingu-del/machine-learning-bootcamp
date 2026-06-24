import random


def guess_number():
    nr = random.randint(1, 99)
    print("This is an interactive guessing game!")
    print("You have to guess a number between 1 and 99.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    attempts = 0
    while True:
        user_input = input("What's your guess between 1 and 99?\n")
        if user_input == "exit":
            print("Goodbye!")
            break
        try:
            guess = int(user_input)
            if guess < 1 or guess > 99:
                print("Please enter a number between 1 and 99.")
                continue
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue

        attempts += 1
        if guess < nr:
            print("Too low!")
        elif guess > nr:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number "
                  f"{nr} in {attempts} attempts.")
            break


def main():
    guess_number()


if __name__ == "__main__":
    main()
