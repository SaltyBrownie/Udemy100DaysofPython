# hangman game
# Goal is to get the user to guess all the letters before the full image of hangman is drawn

# Step 1
import random
import hangman_art
import hangman_words

# stages art from 0 to 6
# logo at 0
print(hangman_art.logo)
lives = 6
word_list = hangman_words.word_list  # string only replace with a API of dictionary words

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
Computer_Choice = random.choice(word_list)  # Computer_choice is the selected work

# Testing CODE
#print("Word is " + Computer_Choice)

hangman_art.stages[lives]  # imported from hangman_art.py file
art_number = 0
print(hangman_art.stages[art_number])

# initialise
display = []
guessed_alphabets = []
Game_Condition = "win"

for Max_length in Computer_Choice:
    display += "_"
end_of_game = False
# heck if display list works
print(display)  # display the _ spaces
while not end_of_game:

    #  Ask the user to guess a letter and assign their answer to a variable called guess.
    #  Make guess lowercase.
    guess = input("Guess a letter: ").lower()
    if guess in display:  # check with display
        print(f"You have already tried the letter {guess}")
    word_length = len(Computer_Choice)
    for position in range(word_length):
        letter = Computer_Choice[position]  # change to letter
        if guess == letter:
            display[position] = guess

        if guess not in guessed_alphabets:  # - guessed letters
            guessed_alphabets.append(guess)

    if guess not in Computer_Choice:
        print(f"Wrong! Word does not contain {guess}")
        art_number += 1
        print(hangman_art.stages[art_number], "\n")
        lives -= 1
        print(f"lives left: {lives}")

    print("\n", display, "\n")
    print("Guessed words", guessed_alphabets)

    if "_" not in display:
        end_of_game = True
        print(f"Congratulations! You have {Game_Condition}!")
    elif lives == 0:
        end_of_game = True
        print(f"{lives} lives left GAME OVER!")
        print("The Word Was", Computer_Choice)
