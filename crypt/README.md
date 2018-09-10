# Crypt
In this lesson, students will write some functions that encrypt and decrypt information.

## Recommended Prerequisite Modules
* mult
* div
* pal
* inventory

## Essential Questions
* How safe is information stored on computers?
* When should data be encrypted?
* What encryption methods are most appropriate for a given use case?

## Resources
* Python v.3.x
* **IDLE *and* Terminal**

## Skills
* Encryption
* Security Awareness
* Error Handling
* Command-line arguments

## Instructional suggestions
Encryption is a deep topic in Computer Science. With new security concerns every day, the need to understand encryption only increases. The actual methods of encryption in use by programmers and security specialists are quite complex, but this module gives a basic understanding of the concept: plain-text information input runs through an algorithm that encodes the information so it is not easily readable.

A **Caesar Cipher** is one of the oldest and simplest methods of encryption. It is, of course, also one of the weakest—breakable with just a little time and knowledge of the alphabet. Nevertheless, it serves as a good introduction to encryption. In a Caesar Cipher, letters in a phrase are "shifted" up or down the alphabet a given number of spaces, turning the resulting words into nonsense. A shift of 4 turns "The quick brown fox jumps over the lazy dog" into:

    Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk

Keen-eyed observers will notice that "xli" appears twice, suggesting this word is common. "The" is the most common three-letter word in English, and is the best guess as to what "xli" translates to. With that information, we can quite easily decrypt the rest of a Caesar Cipher. There are ways to fix this, but we'll get there.

Students could begin with a pen-and-paper exercise in creating Caesar Ciphers. This is usually a lot of fun, and familiarizes them with the steps necessary to create a cipher.

Once the ciphers have been made, you can have students share their ciphers and see if their classmates can decrypt them. Then, ask students to write down the steps necessary to create a cipher. These instructions will serve them well as they produce the Python programs in this lesson.

### crypt-1

#### Command-line Arguments
A lot of new things are going on in this program. To start, the first two lines import the external modules `sys` and `string`. `sys` ties in to the computer's system-level operations. We use this module to gain access to the `argv` array (aka list). In UNIX-like systems, we run commands with optional arguments or options after the command name. Take a simple command like `cd`. When we use this command, we pass an argument to it—the directory we want to switch to.

Command | Arguments
-- | --
`cd` | `Desktop`
`apt-get install` | `firefox python`
`curl` | `-O "https://wordpress.org/latest.zip"`

As the table above shows, we can have more than one argument passed to a command; arguments are separated by spaces.

`sys.argv` collects the arguments passed to the command line into a single list. the first element (index 0) is the program itself. So to get the arguments, we start with `sys.argv[1]`. That lets us call the Python program this way:

    python3 crypt-1.py 4 "The quick brown fox jumped over the lazy dog"

It's important here to consider scope: `crypt-1.py` is an argument for `python3`, and `4` and `"The quick brown fox jumped over the lazy dog"` are arguments for `crypt-1.py`.

Command | Arguments
-- | --
`python3` | `crypt-1.py`
`crypt-1.py` | `4 "The quick brown fox jumped over the lazy dog"`

`4` refers to the shift count for the cipher, followed by the phrase to encrypt.

#### Error Checking
We can't trust users to give us good input. Instead, we have to anticipate where users might make mistakes and handle them in the code. In Python, we can use the `try`/`except` block to catch errors and deal with them before they crash the program.

For instance, we have no guarantee that users will call the encryption program with the right number of arguments. So we'll attempt to assign the correct arguments to variables, but if it fails, we have to have a strategy to continue. Here, we will set `shift_count` to 0 if `shift_count` is missing or not parseable as an integer. We'll also exit with a helpful message if the phrase to encrypt is missing.

Have students brainstorm where else in the program errors might occur. For instance, the `ascii_lowercase` and `ascii_uppercase` strings we use in the program don't include punctuation. So how should we handle a phrase with punctuation—including spaces?

### crypt-2
In the first version of the program, each character was "shifted" down the alphabet one-at-a-time. This made the `shift()` function very clean, but it also made the program do a lot of work throughout its runtime. Because this operation is so repetitive, we can save ourselves some work by creating a "memory" of which input letters match which output letters. We do this with a **dictionary**, another kind of iterable like lists and tuples.

#### Dictionaries
In list and tuples, the only way to refer to a specific element is by its position, or **index**. That can be troublesome if you don't know the index.

Dictionaries use key/value pairs to store information. Instead of using an index to refer to an element, we use the key. So we can create a dictionary using the alphabet as keys, and the shifted alphabet as the values. A shift of 1 then would resut in a dictionary such that:

    >>> library["a"]
    >>> 'b'

This version of the program makes a dictionary of lowercase and capital letters once, and uses it to encrypt the message. This is much more efficient than running the old `shift()` function.

### cryptos
Because of the weakness of the Caesar Cipher, we can use a random assignment of the alphabet to our new encryption—essentially a shuffle of the alphabet. That way, no one can determine from a single letter or word exactly how to decrypt the message. This cipher is still weak enough that it would take only a little time (a day at most) to decrypt a message by hand. A computer could do it in perhaps less than a second.

But the concept here is more important than the specific implementation: we're going to create a key as a separate file that we can share with others so they can decrypt a message.

We'll write the program so that it can also decrypt messages. In fact, we'll write it so the program can do lots of things from the command line depending on the options we pass it.

From a results standpoint want the program to work like this:

    # cryptos --encrypt "Phrase to encrypt"
    # cryptos --decrypt "Tlvewi xs higvctx" --key /path/to/key.json
    # cryptos --keygen

If this is how we want the command-line options to work, we need to use a new module: `argparser`. You can read about this module in the [Python docs](https://docs.python.org/3/library/argparse.html#module-argparse)

#### Shell scripts
Cryptos is a shell script. You'll notice that it doesn't end in `.py`. Additionally, the very first line of code looks very weird:

    #!/usr/bin/python

This line is known as a "shebang". It tells the operating system what shell to use to interpret the code inside. Python is not the only option, but it's the one we'll use to make this utility. The rest of the code should be fairly familiar, just differently structurd because of `argparse`.

This is not necessarily code that students would write at this level. However, it's incredibly helpful to see programs like this, since it hints at structure of programs we use every day.
