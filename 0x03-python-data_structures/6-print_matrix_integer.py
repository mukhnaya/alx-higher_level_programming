#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    pau = len(matrix[0])
    for jul in range(pau):
        for mos in matrix[jul]:
            print("{:d}".format(mos), end=" ")
        print()
