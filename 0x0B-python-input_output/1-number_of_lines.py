#!/usr/bin/python3


def number_of_lines(filename=""):
    """ defining number of lines """
    with open(filename, "r", encoding="UTF8") as f:
        count = 0
        for line in f:
            count += 1
        return count
