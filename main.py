from art import logo
from random import randint
print(logo)
random_number = randint(1, 100)

def compare(guess_number):
    global random_number
    if random_number > guess_number:
        return "Too low."
    elif random_number < guess_number:
        return "Too high."
    else:
        return f"You got it! The answer was {guess_number}"

def play_game():
    global random_number
    print("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {random_number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempt = 10
        while attempt > 0 :
            print(f"You have {attempt} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
            condition = compare(guess_number)
            print(condition)
            if condition == f"You got it! The answer was {guess_number}":
                attempt = 0
            attempt -= 1
            if attempt > 0:
                print("Guess again.")
        print("You've run out of guesses, you lose.")
    elif difficulty == "hard":
        attempt = 5
        while attempt > 0 :
            print(f"You have {attempt} attempts remaining to guess the number.")
            guess_number = int(input("Make a guess: "))
            condition = compare(guess_number)
            print(condition)
            if condition == f"You got it! The answer was {guess_number}":
                attempt = 0
            attempt -= 1
            if attempt > 0:
                print("Guess again.")
        print("You've run out of guesses, you lose.")
                
play_game()
