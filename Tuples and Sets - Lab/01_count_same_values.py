def count_occurrences(numbers):
    occurrences = {}
    for number in numbers:
        occurrences[number] = occurrences.get(number, 0) + 1
    return occurrences

if __name__ == "__main__":
    numbers = input("Enter numbers separated by space: ").split()
    occurrences = count_occurrences(numbers)

    for number, count in occurrences.items():
        print(f"{float(number):.1f} - {count} times")
