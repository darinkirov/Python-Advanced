def read_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def calculate_column_sums(matrix):
    columns = len(matrix[0])
    column_sums = [0] * columns
    for row in matrix:
        for i in range(columns):
            column_sums[i] += row[i]
    return column_sums

if __name__ == "__main__":
    rows, columns = map(int, input("Enter the matrix sizes (rows, columns): ").split(", "))
    matrix = read_matrix(rows, columns)

    column_sums = calculate_column_sums(matrix)

    for sum in column_sums:
        print(sum)
