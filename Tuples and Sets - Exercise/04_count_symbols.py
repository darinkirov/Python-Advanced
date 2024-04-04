def count_character_occurrences(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

if __name__ == "__main__":
    text = input("Enter a text: ")
    char_count = count_character_occurrences(text)

    sorted_char_count = sorted(char_count.items())

    for char, count in sorted_char_count:
        print(f"{char}: {count}")
