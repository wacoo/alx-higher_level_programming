#!/usr/bin/python3

"""Create a class that inherits from list"""


class MyList(list):
    """ print sorted list """
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
