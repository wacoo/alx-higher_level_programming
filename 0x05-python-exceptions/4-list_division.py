#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n = 0
    nl = []
    for idx in range(0, list_length):
        try:
            n = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            n = 0
            print("division by 0")
        except TypeError:
            n = 0
            print("wrong type")
        except IndexError:
            n = 0
            print("out of range")
        finally:
            nl.append(n)
    return nl
