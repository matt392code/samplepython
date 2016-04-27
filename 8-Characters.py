# Program to measure the number of letters in a word
print ("Checking to see if words in list are longer than 8 characters.")
# Open the text file and import it into the file object
alphafile = open("wordfile.txt")
# Do the following for each line in the file
for line in alphafile:
    # Remove whitespace characters from beginning and end of line
    # Then place the line into variable "word"
    word = line.strip()
    # Get the number of characters in a word
    # And place into varible "lengthofword"
    lengthofword = len(word)
    # Check to see of the length of the word is longer than 8 characters
    # If it is, print out the word
    if lengthofword > 8:
        print("Word longer than 8 characters:", word)
