#Will take a word list and pull out all words that have 5 letters.  Then will save it as output.txt
#varibles

# Open the input file
with open("web2", "r") as input_file:
    # Open the output file
    with open("output1.txt", "w") as output_file:
        # Loop over each line in the input file
        for line in input_file:
            # Split the line into words
            words = line.strip().split()
            # Loop over each word
            for word in words:
                # Check if the word has five letters
                if len(word) == 5:
                    # Write the word to the output file
                    output_file.write(word + "\n")
