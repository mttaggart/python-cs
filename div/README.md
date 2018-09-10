# Divide
In this lesson, students will build on what they learned in **mult** to do integer
division.

## Recommended Prerequisite Modules
* mult

## Essential Questions
* How does division actually work?
* What strategies help us translate human processes to computer instructions?

## Resources
* Python v.3.x
* IDLE or Terminal

## Skills
* `while` loops

## Instructional Suggestions

This module is built around a simple question: "If multiplication is repeated
addition, is division repeated subtraction?" Let students grapple with that one
for a while.  If it's true, then they should be able to modify the `mult` program
to easily "divide." It will work in limited circumstances, but not all. There's
a bit more to it than replacing + with -. I find using a number line to explain
multiplication vs. division very helpful.

Moving across the number line involves 4 pieces of information:
1. Our starting point
2. Our destination
3. The size of our steps
4. How many steps we're taking

Only 3 of 4 are necessary to move across the number line. The unknown element
determines what kind of operation it is. Think about multiplication. We know our
starting point (the first term); we know the size of our steps (the second term);
 and we know how many steps we're taking (the first term again). Some of these are
 interchangeable thanks to the commutative property. The unknown is the destination.

 Now consider division. We know our starting point. Do we know our destination?
 We do, actually, but most students won't get this right away. Our destination is
 0, since we're trying to split the number line into equal parts all the way from
 the dividend to 0. The divisor accounts for the size of our steps. What's unknown
 is how many steps we're taking. The quotient of a division problem is just a count
 of how many equally sized steps it takes to walk back from the dividend to 0.

 Armed with this concept, students should be able to use a `while` loop to produce
 a simple integer division algorithm—even accounting for remainders.

 ### div-1.py
 A simple switch of + to - of the code from mult-5.py. It will work sometimes, but
 rarely. It isn't the correct algorithm for this. Often you'll notice the answer
 comes back negative. But we *know* we have to stop at 0. How can we do that?

 The easiest way is to use the arrival at 0 as a condition to stop our looping.
 That's what `while` loops are for.

 ### div-2.py
 Here two things have changed. First, a `while` loop replaces the `for` loop.
`while` loops require a condition to continue looping. In this case, we check
if another subtraction of the divisor from the dividend would result take the
dividend below 0. We increment the quotient each time through the loop, thereby
counting the "steps".

The coolest part of this algorithm is how subtracting from the dividend until
doing so would take us below 0 leaves us with a shrunken dividend, also known as
a remainder. We get that for free by structuring the algorithm this way.
