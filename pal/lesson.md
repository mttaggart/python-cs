# Palindromes
In this lesson, students will write a recursive function that determines whether
a given string is a palindrome.

## Recommended Prerequisite Modules
* mult
* inventory

## Essential Questions
* What makes an algorithm recursive?
* When would we want to use a recursive algorithm?

## Resources
* Python v.3.x
* IDLE or Terminal

## Skills
* `for`/`while` loops
* functions
* string manipulation

## Instructional suggestions
Let's get this out of the way right now: Python's string manipulation abilities
give us a ridiculously easy way of checking for simple palindromes. But that's
not the point here. We're after an understanding of recursive algorithms. Why?
Recursion is all about taking large problems and breaking them down into
smaller, eminently solvable problems.

Start off by asking students how they mentally determine whether a word or
phrase is a palindrome. Odds are you'll get something like "Check the start and
end of the phrase; see if they match; keep going." That's about right for the
computer programmy version as well. Since this checking-beginning-and-end deal
is a repetitive process, your students' instincts should tell them right away
that they'll need a loop. Now, this is doable with a `for` loop, but it's so
messy as to be confusing.

Rather, consider the simplest palindrome: a one-character string. We know for
certain that every one-character string is a palindrome. So our algorithm should
return `True` without any other work if it encounters a one-character string.

What about a two-character string? Here we do the classic checking first
character against second character. If they match, `True`; if not, `False`.

These two are known as "base cases"—the simplest form(s) of a given problem in
a recursive algorithm. They're the floor, so to speak, of our recursion.

## pal-1
This file uses an iterative approach to finding a palindrome. Nothing different
here except for the string slicing. Strings, like lists, can be accessed by index using brackets.

The strategy for this algorithm is no different than the strategy for the recursive algorithm coming up next: take a big string and slice it up into tinier and  tinier ones until we arrive at a mismatch between beginning and end, or a base case.

## pal-2
Here we use recursion rather than iteration. Note that we return a call to the function if `test` doesn't match a base case but still a candidate for a palindromicity.

## pal-race
This last program demonstrates the speed difference between iteration and recursion. The `time-test` function takes 3 arguments: a function to test, a label for the function, and the argument to pass to the function. Using the `time` module, we measure the time elapsed between the start and end of the function. 
