#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    ln = len(argv)
    # print(ln, '=', argv[2])
    ls = ["+", "-", "*", "/"]
    if (ln != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ls:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
        elif argv[2] == '-':
            print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
        elif argv[2] == '*':
            print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
        elif argv[2] == '/':
            print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
        exit(0)
