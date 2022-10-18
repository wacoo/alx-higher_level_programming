#!/usr/bin/python3

""" Locked class """


class LockedClass:
    """ Prevents user form instantiating a lockedClass
        attribute other than first_name """
    __slots__ = ["first_name"]
