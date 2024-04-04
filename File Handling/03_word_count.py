from collections import Counter

# Read words from words.txt and convert to lowercase
with open("words.txt", "r") as words_file:
    words = words_file.read().lower().split()

# Read text from text.txt and convert to lowercase
with open("text.txt", "r") as text_file:
    text = text_file.read().lower().split()

# Count occurrences of each word in text
word_counts = Counter(text)

# Sort words by frequency in descending order
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Write results to result.txt
with open("result.txt", "w") as result_file:
    for word, count in sorted_words:
        if word in words:
            result_file.write(f"{word}: {count}\n")
