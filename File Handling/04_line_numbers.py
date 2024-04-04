import string

# Function to count letters and punctuation marks
def count_letters_and_punctuation(text):
    letter_count = sum(1 for char in text if char.isalpha())
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    return letter_count, punctuation_count

# Read text from input file
with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

# Count letters and punctuation marks for each line
result_lines = []
total_letter_count = 0
total_punctuation_count = 0
for i, line in enumerate(lines, start=1):
    letter_count, punctuation_count = count_letters_and_punctuation(line)
    total_letter_count += letter_count
    total_punctuation_count += punctuation_count
    result_lines.append(f"{i}: {line.strip()} (Letters: {letter_count}, Punctuation: {punctuation_count})")

# Write results to output file
with open("output.txt", "w") as output_file:
    output_file.write("\n".join(result_lines))
    output_file.write(f"\n\nTotal letter count: {total_letter_count}\nTotal punctuation count: {total_punctuation_count}\n")
