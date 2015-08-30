# Multiply and Divide
In this lesson, students will use Python to discover that all complex math operations are just implementations of addition/subtraction Well, really addition.

## Essential Questions
* How are complex mathematical operations just repetitions of simpler ones?
* How can we use programming to take large problems and reduce them to smaller ones?

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
two numbers and returns the product of repeatedly adding one to the other.

### mult-1.py
This first program demonstrates how to use a simple `for` loop.
The values for x and y are hardcoded, and there's no way for the user to
enter them during runtime. Here we're just focusing on the loop.

### mult-2.py
The only significant change here is the introduction of `input()`, allowing users
to enter the numbers they want to multiply at runtime, rather than editing the
source code.
