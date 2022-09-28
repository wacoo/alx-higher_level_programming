#!/usr/bin/python3
def roman_to_int(roman_string):
    n = 0
    if roman_string is None or type(roman_string) != str:
        return 0

    rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = [rn[x] for x in roman_string]
    val.append(0)
    for j in range(len(val) - 1):
        if val[j] >= val[j + 1]:
            n += val[j]
        else:
            n -= val[j]
    return n
