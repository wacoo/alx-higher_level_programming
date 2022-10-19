#!/usr/bin/python3

"""divide a matrix"""


def matrix_divided(matrix, div):
    row_l = 0
    flag = False
    newm = []
    lst = []
    st = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        if not flag:
            row_l = len(i)
            flag = True
        elif row_l != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")

        for j in range(0, len(i)):
            if (type(i[j]) == float):
                i[j] = int(i[j])
            if type(i[j]) != int:
                raise TypeError(st)
            lst.append(round(i[j] / div, 2))
        newm.append(lst)
        lst = []
    return newm
