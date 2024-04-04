def filter_even_numbers(matrix):
    return [[num for num in row if num % 2 == 0] for row in matrix]

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

    new_matrix = filter_even_numbers(matrix)

    for row in new_matrix:
        print(" ".join(map(str, row)))
