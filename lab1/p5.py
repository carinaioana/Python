
def spiral_matrix_to_string(m):
    result = []
    while m:
        # Add the first row to the result
        result.extend(m[0])
        # Remove the first row
        m.pop(0)

        # Rotate the matrix 90 degrees counterclockwise
        m = list(map(list, zip(*m)))[::-1]

    return ''.join(result)


matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result_string = spiral_matrix_to_string(matrix)
print(result_string)