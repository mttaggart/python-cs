"""
One last thing: let's give our user a way to cleanly print the items in the
inventory.
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

def print_inventory():
    """
    Prints each item in the inventory on a new line.
    """
    if len(inventory) == 0:
        print("The inventory is empty!")
    else:
        print("The inventory contains: ")
        for item in inventory:
            print(item)
