def reverse_integers(string_of_integers):
    integers = string_of_integers.split()
    stack = []
    for integer in integers:
        stack.append(integer)
    reversed_integers = []
    while stack:
        reversed_integers.append(stack.pop())
    return ' '.join(reversed_integers)

if __name__ == "__main__":
    string_of_integers = input("Enter integers separated by space: ")
    reversed_integers = reverse_integers(string_of_integers)
    print("Reversed integers:", reversed_integers)
