"""
Time to introduce functions! We will use a function get_values() to get the
terms to multiply, then call the functions.
"""

def get_values():
    """
    Retrieves two values to multiply
    """

    x = input("What is the first number? ")
    y = input("What is the second number? ")
    return (x,y) #What is this? It's a new data type: a "tuple"

#Here's where we call the functions we defined above.
values = get_values() #We store the result of the function in values.
product = 0

#Now we take those two numbers and feed them through a loop
for i in range(values[0]):
    product += values[1]

print(product)
