def find_obstructed_seats(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    obstructed_seats = []

    for j in range(columns):
        current_height = 0
        for i in range(rows):
            if matrix[i][j] > current_height:
                current_height = matrix[i][j]
            else:
                obstructed_seats.append((i, j))

    return obstructed_seats


stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

seats = find_obstructed_seats(stadium)
print(seats)
