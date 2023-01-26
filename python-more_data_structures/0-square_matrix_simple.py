#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for column in row:
            new_row.append(new_matrix)
            new_matrix.append(column**2)
    return new_matrix
    
    
    