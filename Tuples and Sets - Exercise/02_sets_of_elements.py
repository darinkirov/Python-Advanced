def find_common_elements(n, m, set1, set2):
    common_elements = set1 & set2
    return common_elements

if __name__ == "__main__":
    n, m = map(int, input("Enter the lengths of the two sets (n and m): ").split())
    set1 = set(map(int, input("Enter the elements of the first set: ").split()))
    set2 = set(map(int, input("Enter the elements of the second set: ").split()))

    common_elements = find_common_elements(n, m, set1, set2)

    for element in common_elements:
        print(element)
