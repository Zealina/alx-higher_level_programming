#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == 0:
                print("{}".format(matrix[i][j]), end="")
                continue
            print(" {}".format(matrix[i][j]), end="")
        print("")
