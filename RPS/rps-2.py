"""
In this version, we are going to use a loop to allow us to keep score over
multiple contests between computer and human.
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

# We start our wins/losses/ties at 0.
# When we start out variables in this way it is called 'initializing' the variable.
wins = 0
losses = 0
ties = 0

# We will also initialize player_choice. You'll see why in a moment.
player_choice = "" # In this case, initializing to an empty string. This is common.

while player_choice != "quit":
    """
    Our loop will run as long as the player does not enter 'quit'.
    But we couldn't have written our while statement that way without creating
    the player_choice variable beforehand!
    """
    #It's a good idea to give players some instructions
    print("Choose rock, paper, scissors, or 'quit' to quit.")
    player_choice = input("Rock, paper, or scissors? ").lower().strip()

    # Here we have a problem. 'Quit' isn't in the choices. We need to handle it.
    if player_choice not in choices:
        # This is how we handle it: a nested conditional statement
        if player_choice == "quit":
            print("Goodbye!")
            break
        else:
            print("You must choose r, p, or s!")
    else:
        # In these conditionals, we'll have to increment wins/losses
        computer_choice = random.choice(choices)
        print("Computer chose " + computer_choice)
        if beats[player_choice] == computer_choice:
            print("You win!")
            wins += 1
        elif player_choice == computer_choice:
            print("Tie!")
            ties += 1
        else:
            print("You lose!")
            losses += 1

# We're now outside the loop. Everything below only happens once you enter 'quit'.
print("Total score:")
print("Wins:", wins)
print("Losses:", losses)
print("Ties:", ties)
