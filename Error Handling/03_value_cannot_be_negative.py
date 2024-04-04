class ValueCannotBeNegative(Exception):
    pass

def read_numbers():
    numbers = []
    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        if num < 0:
            raise ValueCannotBeNegative("Negative numbers are not allowed")
        numbers.append(num)
    return numbers

try:
    numbers = read_numbers()
    print("Numbers entered:", numbers)
except ValueCannotBeNegative as e:
    print(e)
