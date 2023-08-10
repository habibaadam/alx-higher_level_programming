#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg = sys.argv
    s = len(arg) - 1

    if s > 1:
        print("{} arguments:".format(s))
        for h in range(1, s + 1):
            print("{}: {}".format(h, arg[h]))

    elif s == 0:
        print("{} arguments.".format(s))

    else:
        print("{} argument:".format(s))
        print("{}: {}".format(s, arg[1]))
