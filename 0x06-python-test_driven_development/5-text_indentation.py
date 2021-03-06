#!/usr/bin/python3
""" text_indentation function that indents """


def text_indentation(text):
    """ text_indentation """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.split("\n")
    for string in range(0, len(text)):
        print("{:s}".format(text[string].strip()),
              end=("" if (string == len(text) - 1) else "\n"))
