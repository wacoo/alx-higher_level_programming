#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    myl = matrix[:]
    for i in range(len(matrix)):
        myl[i] = list(map(lambda x: x**2, matrix[i]))
    return myl
