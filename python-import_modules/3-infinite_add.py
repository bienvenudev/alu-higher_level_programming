#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    if len(argv) <= 1:
        print(0)
    elif len(argv) > 1:
        for i in range(len(argv)):
            if i == 0:
                continue
            else:
                result += int(argv[i])
print('{}'.format(result))
