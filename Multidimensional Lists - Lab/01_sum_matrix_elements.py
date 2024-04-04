def read_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def calculate_sum(matrix):
    total_sum = sum(sum(row) for row in matrix)
    return total_sum

if __name__ == "__main__":
    rows, columns = map(int, input("Enter the matrix sizes (rows, columns): ").split(", "))
    matrix = read_matrix(rows, columns)

    total_sum = calculate_sum(matrix)

    print(f"Sum of all numbers in the matrix: {total_sum}")
    print("Matrix:")
    print_matrix(matrix)
