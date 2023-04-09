# Read in the letter counts from the letter_counts.txt file
with open("letter_counts.txt", "r") as input_file:
    # Initialize a dictionary to store the letter counts
    letter_counts = {}
    # Loop over each line in the input file
    for line in input_file:
        # Split the line into a letter and a count
        letter, count = line.strip().split(": ")
        # Convert the count to an integer and store it in the letter_counts dictionary
        letter_counts[letter] = int(count)

# Read in the list of words from the words_five_lower.txt file
with open("words_five_lower.txt", "r") as input_file:
    # Initialize a dictionary to store the word rankings
    word_rankings = {}
    # Loop over each line in the input file
    for line in input_file:
        # Strip any newline characters from the line and convert it to a set of letters
        word_letters = set(line.strip())
        # Compute the total letter count for the word
        total_count = sum(letter_counts.get(letter, 0) for letter in word_letters)
        # Store the word and its ranking in the word_rankings dictionary
        word_rankings[line.strip()] = total_count

# Print the top 10 words by letter count ranking
print("Top 10 words by letter count ranking:")
for word, ranking in sorted(word_rankings.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{word}: {ranking}")
