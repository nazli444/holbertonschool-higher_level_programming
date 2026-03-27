#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in matrix:
        for n in range(0, len(k)):
            if n == len(k) - 1:
                print("{:d}".format(k[n]), end="")
            else:
                print("{:d}".format(k[n]), end=" ")
        print()
