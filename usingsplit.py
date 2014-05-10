# This program will demonstrate the Python split() function.
# It will split a phrase in a string into words

# create string with phrase
hamlet = "To be or not to be, that is the question."

# print the string as entered
print ("The string as entered is:", hamlet)

# split the string and place it into a list called "hamletsplit"
hamletsplit = hamlet.split()

# print out the new list which is the phrase split up by word
print ("The phrase split up is:", hamletsplit)

# print blank line
print () 

# using the len() function, find out how long the list "hamletsplit" is
# then print out each element of the list on its own line, ie:
# hamletsplit[0], hamletsplit[1], hamletsplit[2] etc.
print ("Now we are going to print each element on its own line:")
for alpha in range(len(hamletsplit)):
    print (hamletsplit[alpha])
