#!/usr/bin/python3

"""Create a class that inherits from list"""


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
