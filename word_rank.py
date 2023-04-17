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
    # Ask the user for letters to exclude and include
    exclude_letters = input("Enter any letters to exclude (leave blank for none): ")
    include_letters = input("Enter any letters to include (leave blank for all): ")
    # Loop over each line in the input file
    for line in input_file:
        # Strip any newline characters from the line and convert it to a list of letters
        word_letters = list(line.strip())
        # Exclude any letters specified by the user
        if exclude_letters:
            if any(letter in exclude_letters for letter in word_letters):
                continue
        # Include any letters specified by the user
        if include_letters:
            # Remove any letters that are not included
            word_letters = [letter for letter in word_letters if letter in include_letters]
            if len(word_letters) < len(include_letters):
                continue
        # Skip words with repeated letters
        if len(word_letters) != len(set(word_letters)):
            continue
        # Compute the total letter count for the word
        letter_counts_word = [letter_counts.get(letter, 0) for letter in word_letters]
        total_count = sum(letter_counts_word)
        # Store the word and its ranking in the word_rankings dictionary
        word_rankings[line.strip()
        ] = total_count

# Print the top 10 words by letter count ranking
print("Top 10 words by letter count ranking:")
for word, ranking in sorted(word_rankings.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{word}: {ranking}")
