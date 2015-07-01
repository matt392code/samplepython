# Example of recursion

print "Example of recursion counting upwards. "

# Define the function
def countto100(alpha):
    if alpha == 100:
        print "Counted up to 100."
    elif alpha > 100:
        print "Number entered is greater than 100.  Please enter a number less than 100. "
    else:
        print "You are at number:", alpha
        print "Adding one to previous number now."
        # Recursion below; the function calling itself
        countto100(alpha+1)

numberentered = input("Enter a number less than 100: ")

# Call the function
print ("Call count to 100 function now.")
countto100(numberentered)
