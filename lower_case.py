# Open the input file
with open("output4.txt", "r") as input_file:
    # Open the output file
    with open("words_five_lower.txt", "w") as output_file:
        # Loop over each line in the input file
        for line in input_file:
            # Split the line into words
            words = line.strip().split()
            # Loop over each word
            for word in words:
                # Convert the word to lowercase and write it to the output file
                output_file.write(word.lower() + "\n")
