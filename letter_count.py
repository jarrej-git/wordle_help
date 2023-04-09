# Open the input file
with open("words_five_lower.txt", "r") as input_file:
    # Initialize a dictionary to store the letter frequencies
    letter_counts = {}
    # Loop over each line in the input file
    for line in input_file:
        # Loop over each character in the line
        for char in line.strip():
            # Increment the frequency count for the character
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

# Print the letter frequencies
print("Letter Frequencies:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")

# Write the letter frequencies to a file
with open("letter_counts.txt", "w") as output_file:
    output_file.write("Letter Frequencies:\n")
    for letter, count in letter_counts.items():
        output_file.write(f"{letter}: {count}\n")
