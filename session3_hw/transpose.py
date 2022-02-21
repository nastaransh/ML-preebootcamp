def mat_transpose(a):
    import copy
    b = copy.deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            b[i][j] = a[j][i]
    return b


print(mat_transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
