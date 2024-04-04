def reverse_string(input_string):
    return input_string[::-1]

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)
