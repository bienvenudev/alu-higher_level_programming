#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    arg = ""
    if len(argv) <= 1:
        print("0 arguments.")
    elif len(argv) == 2:
        arg = 'argument'
        print("1 {}:".format(arg))
        print("1: {}".format(argv[1]))
    elif len(argv) > 2:
        arg = 'arguments'
        print(f"{len(argv) - 1} {arg}:")
        for i in range(len(argv)):
            if i == 0:
                continue
            else:
                print(f"{i}: {argv[i]}")
