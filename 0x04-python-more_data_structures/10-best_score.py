#!/usr/bin/python3
def best_score(a_dictionary):
    mx = 0
    k = ""
    if a_dictionary is not None:
        for x, y in a_dictionary.items():
            if y > mx:
                mx = y
                k = x
        return k
    else:
        return None
