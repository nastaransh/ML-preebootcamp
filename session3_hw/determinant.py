

def determinant_recursive(A):
    total = 0
    import copy

    if len(A) == 2 and len(A[0]) == 2:
        ans = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return ans
# create sub-matrix
    for i in range(len(A)):
        sub_mat = copy.deepcopy(A)
        sub_mat = sub_mat[1:]
        for j in range(len(sub_mat)):
            del sub_mat[j][i]

        sign = (-1) ** (i % 2)
        sub_det = determinant_recursive(sub_mat)
        total += sign * A[0][i] * sub_det
    return total


det = determinant_recursive([[1, 2, 3,3], [4, 1, 2, 3], [2, 1, 4, 3], [2, 3, 4, 1]])
print(det)

