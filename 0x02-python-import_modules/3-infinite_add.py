#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    res = 0
    for i in range(1, len(argv)):
        res = res + int(argv[i])
    print("{}".format(res))
