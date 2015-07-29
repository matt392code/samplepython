# Function checks to see if a number is an integer
# using the "isinstance" built-in function
def integertest(alpha):
    if isinstance(alpha, int):
        print(alpha, "is an integer")
    else:
        print(alpha, "is not an integer")

# Function checks to see if it is a positive number
def positivetest(bravo):
    if bravo > 0:
        print (bravo,  "is a positive number")
    elif bravo==0:
        print (bravo,  "is zero")
    else:
        print (bravo,  "is a negative number.")

numberentered = input("Enter a number and this program will check to see if it is an integer and positive: ")

# Call integer function
integertest(numberentered)

# Call positive test function
positivetest(numberentered)
