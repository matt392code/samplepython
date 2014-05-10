# From the book "Learn Python Quickly:" by John Rowland
# Exercise 8: lists
# Created using Python IDLE, the Python IDE

# create an empty list
clubmemberlist=[]
membernumber = 0
enteranother = "y"

# set up while loop to enter names into a list
while (enteranother == "y"):
    newname = input("\nEnter a club member name:  ")
    membernumber = membernumber + 1
    # add name to end of list
    clubmemberlist.append(newname)
    print ("The list now reads: ", clubmemberlist)
    print ("Member number is:  ", membernumber)
    enteranother = input("Would you like to enter another? y or n: ")
    print ("The list in total now reads: ", clubmemberlist)
# end while loop!

# Get the length of the list
print ("Now we are going to get the length of the list. ")
lengthofclubmembers = len(clubmemberlist)
print ("The length of the list is: ", lengthofclubmembers)

# We need to reduce the length number by 1
# because it will fall out of the range of the list if we don't
# Lists start numbering at "0"
lengthofclubmembers = lengthofclubmembers - 1

# this will tell us what number we are on
displaynumber = 1

# Set up loop to print the last 3 names in list
while displaynumber <= 3:
    print("Number: ", lengthofclubmembers+1, "in list is: ", clubmemberlist[lengthofclubmembers])
    # reduce the length of the list by one
    lengthofclubmembers = lengthofclubmembers - 1
    # increase displaynumber by one to work towards 3
    displaynumber = displaynumber + 1
# end while loop!

# Find and remove duplicates in the list
print ("Removing duplicates.")
clubmembernoduplicates = list(set(clubmemberlist))
print ("The list is now: ", clubmembernoduplicates)

print ("Now we are going to sort the list.")
clubmembernoduplicates.sort()
print ("The sorted listis now: ", clubmembernoduplicates)
