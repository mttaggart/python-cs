# Multiply and Divide
In this lesson, students will use Python to discover that all complex math operations are just implementations of addition/subtraction Well, really addition.

## Essential Questions
* How are complex mathematical operations just repetitions of simpler ones?
* How can we use programming to take large problems and reduce them to smaller ones?
* What advantages are there in using functions to write our programs?

## Resources
* Python v.3.x
* IDLE or Terminal

## Skills
* conditionals
* `for` loops
* `while` loops

## Instructional suggestions
Start off outside of Python. In fact, you really don't need a computer to begin
this one. Ask students to write out the steps necessary to multiply 5 by 3
without memorized multiplication facts—they can add, that's it. Have students
do this in groups if possible.

The goal is recognition that repeated addition is, in fact, multiplication.

If that's true, we should be able to write a simple Python program that takes
two integers and returns the product of repeatedly adding one to the other.

### mult-1.py
This first program demonstrates how to use a simple `for` loop.
The values for x and y are hard-coded, and there's no way for the user to
enter them during runtime. Here we're just focusing on the loop.

### mult-2.py
The only significant change here is the introduction of `input()`, allowing users
to enter the integers they want to multiply at runtime, rather than editing the
source code.

### mult-3.py
We want to eventually wrap as much of our code as possible into functions.
This allows us to abstract away some of the complexity of our program, as well
as reusing code without having to rewrite it. It's vital that students understand
the following:

* Defining functions vs. calling functions
* `return` statements

This version of the code also introduces the tuple data type. It may be
worth experimenting with tuples in the shell (indexing, slicing, etc.)
while tackling this one.

### mult-4.py
Here, the multiplication algorithm is wrapped in a function. This might not
seem particularly helpful yet, but it will be soon. Again, functions help to build
robust foundations for our programs without overcomplicating our code.

### mult-5.py
Error checking! We can't trust users to give us good data; we have to be prepared
for non-optimal inputs. Remember that age-old programming maxim: GIGO (Garbage
In, Garbage Out).

### mult-6.py
Only review this if all the concepts so far have been mastered. We're going to
make our program such that it will multiply as many numbers together as we want,
not just two. This requires nested loops and a new way to interpret user input for
multiple values.

Instead of asking for two numbers, we'll ask for a series of integers separated
by commas. So then we have to deal with a big ol' string and pull all our numbers
out. *Then* we have to multiply each successive term together to create a product.

This one's a lot tougher, but the only new things in the program are the `split()`
string function, which returns a `list'. Lists are essentially mutable tuples.

As always, [**read the docs!**](http://docs.python.org).

But this is really where the function structure pays off! We change the guts of
the function, but not the outer instruction flow of the program. That leads to
stability across versions of a program.

Questions to consider in this one:

* What's the deal with those -1s in `mult()`? Why do they work? Are the necessary?
* Is this safe enough? How could I break this code?

The clear bug in this algorithm as written is that, since we use progressive multiplication,
there's no mechanism to handle a 0. If a 0 is introduced as a term, then the algorithm
just moves on to the next term, rather than simply returning 0. Easy fix, but I
left the bug in there for your students to find and remedy.
