def sum_primary_diagonal(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

if __name__ == "__main__":
    N = int(input("Enter the size of the square matrix: "))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    diagonal_sum = sum_primary_diagonal(matrix)

    print("Sum of the primary diagonal:", diagonal_sum)
