# Guess the Number Final Project
# Import
import random as rand
import os
import Art as pic

# Global Variable
# EASY_LIVES = 10
# HARD_LIVES = 5


class Format: #underlines text
    end = '\033[0m'
    underline = '\033[4m'


# Define Functions
def difficulty():
    user_difficulty = input("Pick Difficulty, type 'easy' or 'hard'\n")
    if user_difficulty == "easy":
        difficulty_lives = 10
    elif user_difficulty == "hard":
        difficulty_lives = 5
    else:
        print("You have choose the Extreme Difficulty!")
        difficulty_lives=2
    return difficulty_lives


# Start Game
def start_game():
    # Star Message
    user_guess = int(input("Your Guess is: "))
    return user_guess


def number_conditions(user_guess, generated_number, LIVES):
    if user_guess == generated_number:
        print("Congratulations you have guessed the correct Number!\n")
        # End of game
        return 100
    elif user_guess > generated_number:
        print("Too High! Guess again\n")
        return LIVES - 1
    elif user_guess < generated_number:
        print("Too low! Guess again\n")
        return LIVES - 1

def game_status(score,user_guess,turns):

    print(f"\u0332".join("Status!"))
    print(f"""Score:{score}
Your Guess:{user_guess}
Turns Taken:{turns}""")

# Message to be printed once
print("Welcome to the Number Guessing Game!\nGuess What my integer is to win!\n")
lives = difficulty()
# Generate Random Number
generated_number = rand.randint(0, 100)
#print(f"Computer Generated Number is {generated_number}\n")
# default live condition
Turns = 0
user_guess=1000
while user_guess!=generated_number and lives!=-1:  #
    user_guess = start_game()
    print(Format.underline + f"Game Status!" + Format.end)
    print(f"""Lives:{lives}
Your Guess:{user_guess}
Turns Elapsed:{Turns}""")
    # Cheats Computer Ans: {generated_number}
    # print(f"{type(SG)}user_guess{SG},generated_number{SG}")
    # print(f"user_guess{user_guess},type{type(user_guess)}")

    # Compare the input vs output
    lives = number_conditions(user_guess, generated_number, lives)
    Turns += 1

if lives <= 0:
    print(f"=================================\nYou have lost the game!\n=================================,\nThe Number was {generated_number}!\n=================================\n")
elif user_guess==generated_number:
    print(pic.prize)
    print(f"=================================\nYou have Won! Congratulations\n=================================,\nThe Number was {generated_number}!\n=================================\n")
game_status(lives,user_guess,Turns)
