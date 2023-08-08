#!/usr/bin/python3
for h in range(0, 10):
    for j in range(h + 1, 10):
        if (not (h == 8 and j == 9)):
            print("{}{}".format(h, j), end=", ")
        else:
            print("{}{}".format(h, j))
