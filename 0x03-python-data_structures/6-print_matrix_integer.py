#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cell in row:
            if cell != row[len(row) - 1]:
                print("{}".format(cell), end=' ')
            else:
                print("{}".format(cell), end='')
        print()
