# hangman game
# Goal is to get the user to guess all of the letters before the full image of hangman is drawn

# Step 1
import random

word_list = ["aardvark", "baboon", "camel","word"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
Computer_Choice = random.choice(word_list)
print("Word is "+ Computer_Choice)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# TODO-4 - Check if display list works
display=[]
for letter in Computer_Choice:
    display += "_"
print(display)

if guess == Computer_Choice:
    print("Correct!")
else:
    print(f"Wrong! Word does not contain {guess}")

