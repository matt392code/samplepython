# Program that reads in a file and prints it out by line and field 
alphafile = open("testfile.txt")
for line in alphafile:
    print ("Printing a line: ")
    # Remove the newline character from each line using the strip function
    line = line.strip("\n")
    print (line) 
    # Separate out each word using the split function
    word = line.split()
    print ("Printing by the word: ")
    print (word)
    
# Type this in with a text editor and save file in same directory as importfile.py
# testfile.txt
    #  To be or not to be
    #  That is the question.
    #  Whether tis nobler in the mind
    #  To suffer the slings and arrows of outrageous fortune.
    #  Or to take arms against a sea of troubles.
