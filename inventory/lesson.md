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
Before jumping into any code examples, a simple exercise on indexes will be
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

 ## inventory-1.py
 A very simple program that wraps `append()` in a "setter" function. Load this
 up in IDLE and use `add_item()` with a string to see items get added to the
 `inventory` list. If functions haven't been covered, this is also a great way
 to introduce functions, since the setter is so simple.

 Remember that you can ask IDLE to print `inventory` at any time, and should
 after each call of these functions!

 **Note about setters:** Later in your Python journey, you'll find that Python
 objects have a more formal method of creating "setter" and "getter" methods.
 But for now, we'll use the same term for any function that returns or modifies
 a variable.

 ## inventory-2.py
 Two new functions have been added to play with: `pull_last_item()` and
 `remove_by_name()`. These functions behave exactly as you'd expect. The first
 requires no arguments and simply "pops" off the last-added item to `inventory`.
 The second removes an item by name. It takes a string as an argument.

 But wait: we need to make sure there is such an item to remove, since there's
 nothing stopping a cruel user from telling the function to remove something
 that isn't in the inventory. How do we do that?

 This second function introduces the [try/except](https://docs.python.org/3.4/reference/compound_stmts.html#try)
 model of error handling. Use it well.
