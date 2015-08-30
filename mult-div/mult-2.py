"""
This version uses input() to get x and y from the user. No error checking yet,
and our code is still "naked"—that is, outside of functions. That's not really
a problem, but it will get messy soon.
"""

#Assign the values to the numbers
x = input("What is the first number? ")
y = input("What is the second number? ")

#We need a place to store our product
product = 0

#Now we take those two numbers and feed them through a loop
for i in range(x):
    product += y

print(product)
