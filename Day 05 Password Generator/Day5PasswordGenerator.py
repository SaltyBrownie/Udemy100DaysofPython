import random
from typing import List, Any

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like to have?\n"))
nr_numbers = int(input("How many numbers would you like to have?\n"))
nr_symbols = int(input("How many %%% symbols %%% would you like to have?\n"))
password = ""
for choice_letter in range(nr_letters):
    Letter_Choice = random.choice(letters)
    #print(Letter_Choice)
    password += Letter_Choice
for choice_number in range(nr_numbers):
    Number_choice = random.choice(numbers)  # 0 -9 else list error
    password += Number_choice
for symbols_number in range(nr_symbols):
    symbols_choice = random.choice(symbols)
    password += symbols_choice

print(password)

# Reorder password by shuffle
# Convert string to list and rejoin result
New_password = str
list_password: list[Any] = list(password)
random.shuffle(list_password)

print(''.join(list_password))
