#A simple substitution encryption using alphabet strings
import string
import sys #Hey, a new module!
args = sys.argv
try:
    shift_count = int(sys.argv[1])
except:
    shift_count = 0
try:
    phrase_to_encrypt = sys.argv[2]
except IndexError:
    print("No phrase given!")
    exit()

lowers = string.ascii_lowercase
uppers = string.ascii_uppercase

def shift(char, shift):
    """
    Takes string CHAR and returns the character at shifted index of the alphabet.
    shift('e',1) -> 'f'
    """
    #First thing we want to do is find which alphabet this thing is in, if any.
    if char in string.ascii_lowercase:
        library = string.ascii_lowercase
    elif char in string.ascii_uppercase:
        library = string.ascii_uppercase
    else:
        #Nothing more to be done here; probably a space or punctuation, which we won't mess with.
        return char
    index = library.index(char) + shift
    """
    Our shift is a positive number. So it's entirely possible the resulting index is beyond length of the library. To account for this, we take the difference between our shifted index and the length, essentially wrapping around back to the beginning of the string.
    """
    try:
        return library[index]
    except IndexError:
        return library[index-len(library)]

def encrypt(phrase):
    """
    Takes string PHRASE and returns an encrypted version using SHIFT_COUNT
    """
    encrypted_phrase = ""
    for char in phrase:
        encrypted_phrase += shift(char,shift_count)
    return encrypted_phrase

print(encrypt(phrase_to_encrypt))
