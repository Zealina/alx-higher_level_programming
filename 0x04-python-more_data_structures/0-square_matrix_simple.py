#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    main_list = []
    for i in range(len(matrix)):
        sub_list = list(map(lambda x: x ** 2, matrix[i]))
        main_list.append(sub_list)
    return main_list
