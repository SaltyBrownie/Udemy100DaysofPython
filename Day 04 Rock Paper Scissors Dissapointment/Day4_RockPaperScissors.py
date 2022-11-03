# This is a sample Python script.
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
disappointment = '''
     _ _                             _       _                        _   
    | (_)                           (_)     | |                      | |  
  __| |_ ___  __ _ _ __  _ __   ___  _ _ __ | |_ _ __ ___   ___ _ __ | |_ 
 / _` | / __|/ _` | '_ \| '_ \ / _ \| | '_ \| __| '_ ` _ \ / _ \ '_ \| __|
| (_| | \__ \ (_| | |_) | |_) | (_) | | | | | |_| | | | | |  __/ | | | |_ 
 \__,_|_|___/\__,_| .__/| .__/ \___/|_|_| |_|\__|_| |_| |_|\___|_| |_|\__|
                  | |   | |                                               
                  |_|   |_|                                               
'''
# Write your code below this line 👇
game_images = [rock, paper, scissors, disappointment]
Choice_name = ["Rock", "Paper", "Scissors", "disappointment"]
# print(rock)
# print(paper)
# print(scissors)

user_choice = int(input("Select Choice 0 for rock, 1 for paper , 2 for scissors.\n"))
Computer_choice: int = random.randint(0, 3)
# print(f"Computer Choose:{Choice_name[Computer_choice]}") //debug
if user_choice > 3 or user_choice < 0:
    print("Invalid Number")
elif Computer_choice == 4:
    print(game_images[Computer_choice])
    print("Sorry you have lost due to the computer's mood!")
else:
    # User Print
    print(f"You have Chosen {Choice_name[user_choice]}", game_images[user_choice])
    # Computer print
    print(f"Computer chooses {Choice_name[Computer_choice]}")
    print(game_images[Computer_choice])
    if user_choice == 0 and Computer_choice == 2:
        print("You Win")
    elif Computer_choice > user_choice:
        print("You Lose!")
    elif user_choice == Computer_choice:
        print("Draw! Try Again!")
