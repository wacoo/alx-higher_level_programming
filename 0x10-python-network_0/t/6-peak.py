#!/usr/bin/env python3
# find the peak number

def find_peak(list_of_integers):
    ls = list_of_integers
    l = len(ls)
    #print(l)
    if l > 1:
        for i in range(1, l-1):
            if ls[i-1] <= ls[i] and ls[i+1] <= ls[i]:
                return ls[i]
            #else:
                #return None
    else:
        return None

