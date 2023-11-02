#!/usr/bin/python3
def uppercase(str):

    """This function converts a string to uppercase and
    prints it followed by a new line"""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print('{}'.format(uppercase_char), end="")
    print()
