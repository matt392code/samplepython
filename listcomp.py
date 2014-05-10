# List Comprehension

# Create a list with search pattern
pattern = ["to", "be", "the"]
print ("The pattern to be matched is:", pattern)

#Create string
hamlet = "To be or not to be, that is the question.  Whether tis nobler in the mind to suffer the slings and arrows of outrageous fortune or to take arms against a sea of troubles."

print ("The quote is:")
print (hamlet)

# Split the string into a list
splithamlet = hamlet.split()
print (splithamlet)

# Print a word from the list called "splithamlet" only if it matches one of the words in the the
# list called "pattern"
matches = [word for word in splithamlet if word in pattern]

print ("The list of matches is: ", matches)
