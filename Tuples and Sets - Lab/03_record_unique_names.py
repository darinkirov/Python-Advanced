def print_unique_names(names):
    unique_names = set(names)
    for name in unique_names:
        print(name)

if __name__ == "__main__":
    names = input("Enter a list of names separated by space: ").split()
    print_unique_names(names)
