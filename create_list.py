#Will take a word list and pull out all words that have (length) number of letters.  Then will save it as output.txt
#varibles
length = 5 #sets length of words to extract for new file.  Instead of setting manually below.

# Open the input file
with open("web2", "r") as input_file:
    # Open the output file
    with open("output4.txt", "w") as output_file:
        # Loop over each line in the input file
        for line in input_file:
            # Split the line into words
            words = line.strip().split()
            # Loop over each word
            for word in words:
                # Check if the word has five letters
                if len(word) == length:
                    # Write the word to the output file
                    output_file.write(word + "\n")
