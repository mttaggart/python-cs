"""
Here's some complexity: what if the user gives us a letter in input() and not
a number? Or what if it's an decimal (float) instead of an integer? We need to
validate our inputs.
"""

def get_values():
    """
    Retrieves two values to multiply
    """

    x = input("What is the first number? ")
    y = input("What is the second number? ")
    try:
        #Before, the program would have failed on non-integer input. Now we can catch it.
        int_x = int(x)
        int_y = int(y)
    except ValueError: #If the inputs can't be parsed into
        print("We need two integers to multiply!")
        return get_values() #On an error, we're going to run the function again

    return (x,y)

def mult(terms):
    """
    Takes a 2-element tuple TERMS and multiplies the two terms
    """

    a,b = terms[0], terms[1]
    product = 0

    for i in range(x):
        product += y

    return product

values = get_values()
answer = mult(values)
print(answer)
