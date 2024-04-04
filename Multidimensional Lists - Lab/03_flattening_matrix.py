if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    matrix = [list(map(int, input().split(", "))) for _ in range(rows)]

    flattened_matrix = [num for row in matrix for num in row]

    print(flattened_matrix)
