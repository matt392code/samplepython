# This program will take 2 numbers from the user and
# find the hypotenuse using the Pythagorean theorem

import math

# Function to square the numbers
def squarefunction(length):
    square = length * length
    print "The square of a side is: ", square
    return square
# end of function

# Function to calculate Pythagorean theorem
def pythagorean(aside, bside):
    HypotenuseSquared  = aside + bside
    hypotenuse = math.sqrt(HypotenuseSquared)
    print "The hypotenuse of the 2 sides is: ", hypotenuse
# end of function

# Get the length of the sides from the user
firstside = input("Enter the first side: ")
secondside = input("Enter the second side: ")

# Get the squares of 2 sides
firstsidesquared = squarefunction(firstside)
secondsidesquared = squarefunction(secondside)
# print "The firstside variable is: ", firstside
# print "The secondside variable is: ", secondside

# Put the squares into the Pythagorean function
pythagorean(firstsidesquared, secondsidesquared)

