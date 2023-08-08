#!/usr/bin/python3
for value in range(0, 100):
    if value == 99:
        print("{}".format(value))
    else:
        print("{:02}".format(value), end=", ")
