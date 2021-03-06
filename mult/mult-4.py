"""
Now we'll functionify the multiplication process. This seems like a lot more
code—why bother? As we add features to our program, this strong foundation
will make it easier for us to add complexity.
"""

def get_values():
    """
    Retrieves two values to multiply
    """

    #Now we do the input/conversions to int in one line. What's the risk here?
    x = int(input("What is the first number? "))
    y = int(input("What is the second number? "))
    return (x,y) #What is this? It's a new data type: a "tuple"

def mult(terms):
    """
    Takes a 2-element tuple TERMS and multiplies the two terms
    """
    #We need a place to store our product
    a,b = terms[0], terms[1]
    product = 0

    #Now we take those two numbers and feed them through a loop
    for i in range(a):
        product += b

    return product #Notice that we're returning instead of printing here.

#Here's where we call the functions we defined above.
values = get_values()
answer = mult(values)
print(answer)
