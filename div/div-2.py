"""
Time to fix the div() so it gives right answers.
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

    return (int_x,int_y)

def div(terms):
    """
    Takes a 2 tuple TERMS—dividend and divisor—and returns the quotient.
    This one uses a simple reversal of the mult() function.
    """
    dividend,divisor = terms[0], terms[1]

    quotient = 0

    #We use a a while loop
    while dividend - divisor >= 0:
        dividend -= divisor
        quotient += 1
        #Fun bonus! The divident, after all this subtraction, is actually the remainder.

    return (quotient,dividend)

values = get_values()
answer = div(values)
print(answer)
