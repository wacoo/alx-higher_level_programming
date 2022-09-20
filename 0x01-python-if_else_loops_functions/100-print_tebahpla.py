#!/usr/bin/python3
j = 0
for i in reversed(range(97, 123)):
    if i % 2 == 0:
        j = i
    else:
        j = i - 32
    print("{}".format(chr(j)), end='')
