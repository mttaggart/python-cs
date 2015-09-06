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

`TypeError: 'tuple' object does not support item assignment`

Tuples are *immutable*: they can't be changed once they're set. To do that, we
need to switch to another iterable data type: **lists**.

So using our enterprising collection of captains (or any list of your/your
  students') once more, let's try:

`>>> captains = ["Pike","Kirk","Picard","Sisko","Janeway"]`

Notice the brackets instead of parens? That's how we know it's a list.

Lists have special *methods* associated with them. Most important of these is
`append()`. Let's add another captain (or whatever) to our list:

```
>>> captains.append("Archer")
>>> captains
['Pike','Kirk','Picard','Sisko','Janeway','Archer']
```

And that's how we add new items to a list. Can we remove them?

Yes—within some limits. [Read the docs](https://docs.python.org/3.4/library/stdtypes.html#mutable-sequence-types)
for details on exactly what is possible with mutable sequence types like lists.
 Pay close attention to `pop()`, `insert()`, and `remove()`. Experiment with
 these methods on your test list in the IDLE shell.

 When that's finished, you can move on to the first piece of code:
 `inventory-1.py`
