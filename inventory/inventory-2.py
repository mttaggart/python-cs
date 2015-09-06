"""
Now we'll add two more functions: the first will pull the last thing out of the
inventory using pop(). The second will pull an item out by name. We're going to
make sure there is such an item using try/except.
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

def pull_last_item():
    """
    Removes last added item from the inventory.
    """
    pulled_item = inventory.pop()
    pull_message = "{} pulled from inventory.".format(pulled_item)
    print(pull_message)

def remove_by_name(item):
    """
    Searches inventory for an item and removes it if found.
    """
    try:
        inventory.remove(item)
        print("Removed {} from inventory.".format(item))
    except ValueError:
        print("No such item!")
