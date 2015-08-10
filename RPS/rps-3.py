"""
A lot fewer comments in this one now that you now what you're doing!
"""

import random

beats = {
    "rock":"scissors",
    "paper":"rock",
    "scissors":"paper"
}
choices = list(beats.keys())

wins = 0
losses = 0
ties = 0

# Here come the functions: one for each step in the last version.

def print_score():
    print("Wins:", wins)
    print("Losses:", losses)
    print("Ties:", ties)

def compare(c,p):
    """
    c and p are used here to distinguish the arguments to the function from
    the player_choice and computer_choice variables in main().
    """
    global wins,losses,ties
    print("Computer chose " + c)
    if beats[p] == c:
        print("You win!")
        wins += 1
    elif p == c:
        print("Tie!")
        ties += 1
    else:
        print("You lose!")
        losses += 1

def main():
    """
    Take note how much clearer this is. Also, where'd that while loop go?
    """
    print("Choose rock, paper, scissors, or 'quit' to quit.")
    player_choice = input("Rock, paper, or scissors? ").lower().strip()
    computer_choice = random.choice(choices)
    if player_choice == "quit":
        print("Goodbye!")
        print("Final score:")
        print_score()
    elif player_choice not in choices:
        print("You must choose r, p, or s!")
        main()
    else:
        compare(computer_choice, player_choice)
        main()

main() # This is the line that starts the show.
