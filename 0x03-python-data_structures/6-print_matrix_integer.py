#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    pau = len(matrix[0])
    for jul in range(pau):
        for mos in range(pau):
            if mos < pau -1:
                print("{:d}".format(matrix[jul][mos]), end=" ")
            else:
                print("{:d}".format(matrix[jul][mos]), end="")
        print()
