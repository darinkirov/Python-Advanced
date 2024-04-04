text = input("Enter the text: ")
try:
    times = int(input("Enter the number of times to repeat the text: "))
    print(text * times)
except ValueError:
    print("Variable times must be an integer")
