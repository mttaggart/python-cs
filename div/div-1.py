"""
To begin, we'll reuse the get_values() function from mult. That part's the same,
anyway.
"""

def get_values():
    """
    Retrieves two values to divide
    """

    x = input("What is the divisor? ")
    y = input("What is the dividend? ")
    try:
        #Before, the program would have failed on non-integer input. Now we can catch it.
        int_x = int(x)
        int_y = int(y)
    except ValueError: #If the inputs can't be parsed into
        print("We need two integers to divide!")
        return get_values() #On an error, we're going to run the function again

    return (x,y)

def div(terms):
    """
    Takes a 2 tuple TERMS—dividend and divisor—and returns the quotient.
    This one uses a simple reversal of the mult() function.
    """
    a,b = terms[0], terms[1]
    #obviously we can't start at 0 and subtract; we'll get a negative!
    #Instead we begin at the top—our dividend.
    product = a

    for i in range(x):
        product -= y

    return product
