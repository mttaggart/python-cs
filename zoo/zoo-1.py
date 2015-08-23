from animal import * # Get all the stuff we need from our animal module

dog = Animal("rex") # Create a new instance of Animal and assign it to dog

print(dog.call())

"""
We have to wrap the call() method in print() because the return statement needs
to deliver its payload somewhere.
"""
