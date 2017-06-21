#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """ defining read lines """
    with open(filename, "r", encoding="UTF8") as f:
        num_lines = sum(1 for line in filename)
        if nb_lines <= 0 or nb_lines >= num_lines:
            print(f.read(), end="")
        else:
            for line in range(0, nb_lines):
                print(f.readline(), end="")
