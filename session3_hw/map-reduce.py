from functools import reduce


def mult_matrix(mat1, mat2):
    result = []
    if len(mat1) == len(mat2[0]):
        result = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                result[i][j] = reduce(lambda a, b: a + b,
                                      map(lambda x, y: x * y, mat1[i], [mat2[l][j] for l in range(len(mat1[0]))]))

    return result
