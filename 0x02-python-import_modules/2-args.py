#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1

    if count == 0:
        print("{:d} argument.".format(count))
    elif count == 1:
        print("{:d} argument:".format(count))
    else:
        print("{:d} arguments:".format(count))
    for i in range(1, count + 1):
        print("{:d}: {:s}".format(i, argv[i]))
