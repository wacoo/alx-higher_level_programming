#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_l = [0] * list_length
    for idx in range(0, list_length):
        try:
            new_l[idx] = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            new_l[idx] = 0
            print("division by 0")
        except TypeError:
            new_l[idx] = 0
            print("wrong type")
        except IndexError:
            new_l[idx] = 0
            print("out of range")
    return new_l
