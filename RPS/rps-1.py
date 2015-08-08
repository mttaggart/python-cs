# A simple rock, paper, scissors script submitted as a demo of easy game-making
# In Python
# Certain parts of this program are functional—that is, written in functions that
# work together. Some parts aren't. As we improve the program, you'll find that
# This functional way of doing things has some real advantages.

import random # We need thr random module for the computer to play

beats = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}

choices = list(beats.keys())

def get_computer_choice():
    return random.choice(choices)

def compare(player_choice,computer_choice):
    """
    Return player victory. True if player wins, False if computer wins.
    """
    return beats[player_choice] == computer_choice

player_choice = input("Rock, paper, or scissors?").lower()

if player_choice not in choices:
    print("You must choose r, p, or s!")
else:
    computer_choice = get_computer_choice()
    if compare(player_choice,computer_choice):
        print("You win!")
    else:
        print("You lose")
