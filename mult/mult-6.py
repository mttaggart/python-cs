"""
Here's some complexity: what if the user gives us a letter in input() and not
a number? Or what if it's an decimal (float) instead of an integer? We need to
validate our inputs.
"""

def get_values():
    """
    Retrieves two values to multiply
    """

    user_values = input("On the next line, enter the values to multiply,\
separated by commas. \n>> ")
    input_list = user_values.split(",")
    final_list = []
    #We've split the user's input into a list, but have no idea if it's any good.
    #Let's check. If it's good, we'll add the integer to the final list.

    for val in input_list:
        try:
            final_list.append(int(val))
        except ValueError:
            print("We need the list to be all integers!")
            return get_values()
    #Is it alright to return a list instead of a tuple now? They work similarly, so yes.
    return final_list

def mult(terms):
    terms_remaining = terms[::-1] #This is for clarity since we're going in reverse order
    product = terms_remaining.pop()
    for i in range(len(terms)-1):
        current_term = product
        next_term = terms_remaining.pop()
        for o in range(next_term-1):
            print(product)
            product += current_term
    return product


values = get_values()
answer = mult(values)
print(answer)
