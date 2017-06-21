#!/usr/bin/python3


def write_file(filename="", text=""):
    """ defining write_file """
    with open(filename, "w", encoding="UTF8") as f:
        s = str(text)
        return (f.write(s))
