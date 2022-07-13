# this is the "game.py" file...

name = input("Hello Player One. What is your name?")
nl = '\n'
text = f"Hello {name}. Ready? Rock, paper, scissors, shoot!"
print(text)

import random

user_choice = input("Please enter a choice (rock, paper, scissors): ")
user_action = user_choice.casefold()
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print ("That's not a valid play. Please check your spelling")

print("Thank you for playing")