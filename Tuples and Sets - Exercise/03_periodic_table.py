def unique_chemical_elements(n):
    unique_elements = set()

    for _ in range(n):
        compounds = input().split()
        for element in compounds:
            unique_elements.add(element)

    return unique_elements

if __name__ == "__main__":
    n = int(input("Enter the count of input lines: "))
    unique_elements = unique_chemical_elements(n)

    for element in unique_elements:
        print(element)
