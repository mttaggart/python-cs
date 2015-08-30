"""
Time to introduce functions! We will define the steps of our program
functionally, then call the functions.
"""

def get_values():
    """
    Retrieves two values to multiply
    """

    x = input("What is the first number? ")
    y = input("What is the second number? ")
    return (x,y) #What is this? It's a new data type: a "tuple"

def mult(terms):
    """
    Takes a 2-element tuple TERMS and multiplies the two terms
    """
    #We need a place to store our product
    a,b = input_tuple=[0], input_tuple[1]
    product = 0

    #Now we take those two numbers and feed them through a loop
    for i in range(x):
        product += y

    return(product) #Notice that we're returning instead of printing here.

#Here's where we call the functions we defined above.
values = get_values()
answer = mult(values)
print(answer)
