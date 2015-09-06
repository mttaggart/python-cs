"""
In this first list program, we'll simply create an inventory and write a
function to manipulate it. This function is of a sort known as a "setter." It
can also be considered a "wrapper" for the append() method of the list. Why
do we even need a wrapper? Sometimes we like to make the output of a setter more
 user-friendly.
"""

#Initialize the inventory variable to an empty list.
inventory = []

def add_item(item):
    """
    Adds item to inventory.
    """
    inventory.append(item)
    add_message = "{} added to inventory.".format(item)
    print(add_message)
