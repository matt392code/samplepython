# Using Python written by Matt R 
# Released under the GPL
# Define functions first

# Function to test if number is divisible by 3
def testforthree(alpha):
    bravo = alpha%3
    if bravo == 0:
        print "Crackle!",  alpha

# Function to test if number is divisible by 5
def testforfive(charlie):
    delta = charlie%5
    if delta == 0:
        print "Pop!",  charlie

# Function to test if number is divisible by 3 and 5
def testforthreefive(echo):
    foxtrot = echo%3
    golf = echo%5
    if (foxtrot==0) and (golf==0):
        print "CracklePop!",  echo

# Testing the functions to make sure they work
# testforthree(9)
# testforfive(5)
# testforthreefive(15)

# Assign seed number for the loop
hotel = 1

# Set up "while" look to go through numbers 1 to 100
while (hotel <=100):
    print "The current number is: ",  hotel
    # Test the number using functions
    
    # Testing to see if number is divisible by 3
    testforthree(hotel)
    
    # Testing to see if number is divisible by 5
    testforfive(hotel)
    
    #Testing to see if number is divisible by 3 and 5
    testforthreefive(hotel)
    
    # Increase loop number by 1
    hotel = hotel + 1
