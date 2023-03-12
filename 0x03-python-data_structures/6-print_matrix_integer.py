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

matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
