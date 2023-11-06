class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            raise IndexError("Index out of range")

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Index out of range")

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix is not compatible ")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply_transform(self, transform_func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = transform_func(self.data[i][j])

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str


def main():
    matrix = Matrix(3, 3)
    for i in range(3):
        for j in range(3):
            matrix.set(i, j, i * 3 + j + 1)

    print("Original Matrix:")
    print(matrix)

    transposed_matrix = matrix.transpose()
    print("\nTransposed Matrix:")
    print(transposed_matrix)

    other_matrix = Matrix(3, 2)
    for i in range(3):
        for j in range(2):
            other_matrix.set(i, j, i * 2 + j + 1)

    product = matrix.multiply(other_matrix)
    print("\nMatrix Multiplication Result:")
    print(product)

    matrix.apply_transform(lambda x: x * 2)
    print("\nMatrix After Applying Transformation:")
    print(matrix)


if __name__ == "__main__":
    main()

