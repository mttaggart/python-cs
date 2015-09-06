# Inventory
In this lesson, students will become acquainted with iterable data types like
tuples, lists, and dictionaries.

## Recommended Prerequisite Modules
* (none)

## Essential Questions
* What applications do iterable data types have in programming?
* How do you decide to use a tuple, list, or dictionary?

## Resources
* Python v.3.x
* IDLE or Terminal

## Skills

## Instructional Suggestions
Before jumping into any code examples, a simply exercise on indexes will be
 helpful.

Begin by asking students to make lists of things. It doesn't really matter
what the lists are of, just that they're lists. They could be favorite
foods, colors, superheroes—whatever.

With the lists finished, have the students input them into idle in
the following manner:

`>>> captains = ("Pike","Kirk","Picard","Sisko","Janeway")`

They've created their first **tuple**. You can then demonstrate how to access
individual elements of the tuple using the bracket syntax:

```
>>> captains[0]
'Pike'
>>> captains[3]
'Sisko'
>>> captains[-1]
'Janeway'
```

So we can clearly access specific elements of a tuple. Can we change them?
Let's try:

`captains[3] = "Spock"`

Get an error? Maybe something like:

`item tuple does not support item assignment`

Tuples are *immutable*: they can't be changed once they're set. To do that, we
need to switch to another iterable data type: **lists**. 
