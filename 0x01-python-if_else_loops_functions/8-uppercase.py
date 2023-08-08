#!/usr/bin/python3

def uppercase(str):
    for h in range(len(str)):
        code = ord(str[h])
        if code >= 97 and code <= 123:
            code = code - 32
        print("{}".format(chr(code)), end='')
    print()
