#!/usr/bin/python3
'''To divide matrix elements with a number and return new matrix'''
def matrix_divided(matrix, div):
    '''
    divides elements of a matrix
    '''
    if matrix is list:
        '''number of rows of matrix'''
        matrix_rows = len(matrix)
        jos = 0
        while jos < matrix_rows:
            for i in matrix[jos]:
                if (type(i) is not int) | (type(i) is not float):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                break
            jos+=1
        '''len of first row'''
        first_row_len = len(matrix[0])
        mos = 0
        rows_len = 0
        while (mos < matrix_rows):
            rows_len = len(matrix[mos])
            if first_row_len != rows_len:
                raise TypeError("Each row of the matrix must have the same size")
                break
            mos+=1
        if (type(div) is not int) | (type(div) is not float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        new_matrix = [[]]
        for x in range(matrix_rows):
            for y in range(first_row_len):
                res = matrix[x][y] / div
                new_matrix.append(res)
            return new_matrix
