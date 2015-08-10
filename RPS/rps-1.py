"""
A simple rock, paper, scissors script submitted as a demo of easy game-making
In Python.
"""
import random # We need thr random module for the computer to play

# This dictionary relates a choice to what it defeats for easy comparison later.
beats = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}

# Now we make an easy-to-use list of choices from the beats
choices = list(beats.keys())

# Get the player choice from the input command.
# The lower() is used to correct for people typing with capitals.
# The strip() removes any trailing space that might mess us up.
player_choice = input("Rock, paper, or scissors? ").lower().strip()

# Finally, time to compare! But we have to account for cheaters/mistakes.
if player_choice not in choices:
    print("You must choose r, p, or s!")
else:
    # Here we make the computer choose, then compare the two.
    computer_choice = random.choice(choices)
    print("Computer chose " + computer_choice)
    if beats[player_choice] == computer_choice:
        print("You win!")
    elif player_choice == computer_choice:
        print("Tie!")
    else:
        print("You lose!")

"""
This program works, but it's quite limited. Probably its biggest limitation
is that it will only run once. It also doesn't keep score—why would it, since
it only runs once? Our next version of the game will make it more user-friendly.
"""
