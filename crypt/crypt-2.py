#A simple substitution encryption using alphabet strings and dictionaries

"""
Good programming practice tells us to make as few heavy system calls as possible. And where possible, we should front-load the heavy work if it will save us significant time later. crypt-1 called shift() for each character in the phrase. That's a lot of work! Instead, let's make a dictionary that allows us easy lookup of shifted characters right away, without having to do the same operation over and over.
"""
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

def build_shift_library(shift):
    libraries = [string.ascii_lowercase, string.ascii_uppercase]
    shift_library = {}
    for lib in libraries:
        for char in lib:
            index = lib.index(char) + shift
            try:
                shift_library[char] = lib[index]
            except IndexError:
                shift_library[char] = lib[index-len(lib)]
    return shift_library

def encrypt(phrase):
    """
    Takes string PHRASE and returns an encrypted version using SHIFT_COUNT
    """
    shift_library = build_shift_library(shift_count)
    encrypted_phrase = ""
    for char in phrase:
        try:
            encrypted_phrase += shift_library[char]
        except KeyError:
            encrypted_phrase += char
    return encrypted_phrase

print(encrypt(phrase_to_encrypt))
