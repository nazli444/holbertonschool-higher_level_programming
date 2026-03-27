#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for n in matrix:
        h = []
        for k in n:
            h.append(k ** 2)
        new_matrix.append(h)
    return new_matrix
