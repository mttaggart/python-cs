"""
This file will be what we call a 'module'. Other files that we use will reference
this one, so we don't have to keep rewriting our code for each revision of our
zoo. Instead, we'll use the import command to pull this info into other files.

This program will be written using object-oriented programming, or OOP. Simply
put, OOP lets us create structures in our code that are closer to how we think
of things in everyday life.

We can store information that we're working with in these objects.

Variables associated with objects are called properties; Functions associated
with objects are known as methods. Keep these terms in mind as we go through the
code.
"""

# Our base class for making animals.
class Animal:

    """
    In Python, there are certain "magic" methods whose names are reserved for
    specific operations. These magic methods are indicated by the double
    underscores before and after the method name.
    """

    def __init__(self,name):
        """
        __init__ is one of those magic methods. Every object is a member,
        or instance, of a class. __init__ creates a new
        'instance' of a class. Notice that this init takes two arguments, and
        that every method in the Animal class takes self as an argument. We'll
        never use that self when we access these methods.
        """
        self.name = name # We pull the name from the second argument to init
        self.full = True # We create our Animal with a full belly

    def call(self):
        return "I'm a default animal and my name is {}.".format(self.name)

    def is_full(self):
        return self.full

    def eat(self):
        print("Nom nom nom")
        self.full = True
