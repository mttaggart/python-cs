# Root
In this lesson, students will write a function that uses bisection search to determine the square root of a given number.

## Recommended Prerequisite Modules
* mult
* div
* pal

## Essential Questions
* Where can we use bisection search?
* Is Computer Science an exact science?

## Resources
* Python v.3.x
* IDLE or Terminal

## Skills
* Algorithm building

## Instructional suggestions
Imagine you can do math, know what a square root is, but have no memorized multiplication facts. Now find the square root of 16. How do you begin?

Most students would begin with good ol' guess-and-check. That's not a bad idea! But what should the first guess be?

The *possibility space* for the root is between zero and the square. Splitting the space in half is a very strong strategy. There are a few better ones, but this is simple and effective. Let's see how this goes.

    #Find the square root of 16
    >>> Guess 8
    >>> 8*8 = 64
    #Too high; try half of that
    >>> Guess 4
    >>> 4*4 = 16
    #Got it!

That worked out pretty well. What happens when we go to 25?

    #Find the square root of 25
    >>> Guess 12.5
    >>> 12.5 * 12.5 = 156.25
    #Too high; try half of that
    >>> Guess 6.25
    >>> 6.25 * 6.25 = 39.0625
    #Too high; try half of that
    >>> 3.125 * 3.125 = 9.765625
    #Too low; try the midpoint between 3.125 and 6.25
    >>> 4.6875 * 4.6875 = 21.97265625
    #Too low; try the midpoint between 4.6875 and 6.25
    >>> 5.46875 * 5.46875 = 29.9072265625
    #Too high; try the midpoint between 4.6875 and 5.46875
    >>> 5.078125 * 5.078125 = 25.787353515625
    #See the problem here?

Our guess and check method, because of the nature of floating point numbers, will try to get closer and closer, but never get all the way to 25.0000....

## root-1
This program uses bisection search but has no safety for the endless hunting for more precise roots. Let students write and run this program.

The example code searches for 16. Have students write this and enjoy that the algorithm works. Then change it to 25. They'll have to use Ctrl-C to stop the program once it runs amok, but that's a valuable lesson in itself.

##root-2
Here we use `epsilon`—essentially a "close enough" test to see if the algorithm can stop looking. `epsilon` is the degree of precision for our algorithm. Experiment with different values here.

Before showing students the example code, discuss strategies for determining whether the algorithm can stop searching. The key word that should enter the conversation is "difference". Once that word is out there, the notion of using a subtraction operation should become clear.

The sample code also logs how many guesses it took, just for fun.

## root-recur
If students have done the `pal` module, ask them to rewrite this algorithm recursively. The trick here is remembering that you'll have to pass the original *and* the guess through each recursion, so the function will have to take at least two arguments.

You might want to consider implementing the time-test function from `pal` here to see which algorithm is faster.

##Going further
Rootfinding is a deep topic in mathematics, and bisection search, while simple, is not the most efficient. The more advanced algorithms require a little bit more work to implement (The Newton-Raphson algorithm requires derivation), but implementing these in Python would be a fun adventure for the curious.
