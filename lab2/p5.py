def matrix_diagonal(matrix):
    if not matrix:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0

    return matrix


def main():
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    result = matrix_diagonal(m)
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
