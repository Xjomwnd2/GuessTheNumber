# guess_number.py

import random

def play_game():
    print("🎮 Welcome to Guess the Number (Python Edition)!")
    number_to_guess = random.randint(1, 100)
    guess = None

    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < number_to_guess:
                print("Too low! 🔽")
            elif guess > number_to_guess:
                print("Too high! 🔼")
            else:
                print("🎉 Congratulations! You guessed it!")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    play_game()


