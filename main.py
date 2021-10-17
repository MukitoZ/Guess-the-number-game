from art import logo
from random import randint
from replit import clear

#constant variable for attempt
EASY_DIFFICULTY = 10 
MEDIUM_DIFFICULTY = 7
HARD_DIFFICULTY = 5

def compare(random_number, guess_number, lives):
    """Comparing the random_number and guess_number to check if the guess_number is correct or not"""
    if random_number > guess_number:
        print("Too low.")
        return lives - 1
    elif random_number < guess_number:
        print("Too high.")
        return lives - 1
    else:
        print(f"You got it! The answer was {guess_number}")

def attempt():
    difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_DIFFICULTY
    elif difficulty == "medium":
        return MEDIUM_DIFFICULTY
    elif difficulty == "hard":
        return HARD_DIFFICULTY
    else:
        print("Choose the right difficulty!")
        return attempt()

def play_again():
    if input("Do you want to play again? 'y' or 'n': ").lower() == 'y':
        clear()
        play_game()
    else:
        return

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    random_number = randint(1, 100)

    guess_number = 0
    lives = attempt()
    while guess_number != random_number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        lives = compare(random_number, guess_number, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            play_again()
            return
        elif guess_number != random_number:
            print("Guess again.")


play_game()
