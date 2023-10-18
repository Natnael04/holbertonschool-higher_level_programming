#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, element in row:
            print("{:d}".format(element), end=' ')
            if i == len(row) - 1:
                print()
        print()
