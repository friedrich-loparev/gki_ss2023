def iterate_over_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            yield matrix[i][j]
