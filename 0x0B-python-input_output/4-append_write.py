#!/usr/bin/python3


def append_write(filename="", text=""):
    """ defining append_write """
    with open(filename, "a", encoding="UTF8") as f:
        s = str(text)
        return(f.write(s))
