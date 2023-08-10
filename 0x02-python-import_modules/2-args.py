#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argument = sys.argv
    length = len(argument) - 1

    if length > 1:
        print("{} arguments:".format(length))
        for h in range(1, length + 1):
            print("{}: {}".format(h, argument[h]))

    elif length == 0:
        print("{} arguments.".format(length))

    else:
        print("{} arguments.".format(length))
        print("{}: {}".format(length, argument[1]))
