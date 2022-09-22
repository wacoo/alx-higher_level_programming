#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    no = len(argv) - 1
    if no == 1:
        print("{} argument:".format(no))
    elif no == 0:
        print("{} arguments.".format(no))
    else:
        print("{} arguments:".format(no))
    for arg in argv:
        ind = argv.index(arg)
        if ind > 0:
            print("{}: {}".format(ind, arg))
