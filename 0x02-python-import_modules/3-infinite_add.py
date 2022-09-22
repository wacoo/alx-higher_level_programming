#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    res = 0
    for arg in argv:
        if arg.isdigit():
            res = res + int(arg)
    print(res)
