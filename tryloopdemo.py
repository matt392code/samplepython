# Try loop demo
print ("This is a try loop demo.")
loopagain = "yes"

# try loop will catch exceptions if non-integer is entered
while loopagain=="yes":
    while True:
        try:
            numberentered = int(input("Enter an integer number: "))
            # break out of loop if integer entered
            break
            # If a non-integer value entered, consider it a ValueError
        except ValueError:
            print ("Please enter an integer, not a floating point number or letter")
    print ("You entered the following integer:", numberentered)
    loopagain = input("Would you like to try again? enter yes or no: ")
    if loopagain=="no":
        print ("Thank you.")
    else:
        loopagain="yes"
        print ("Starting program again.")
    # end while loop
    
# If integer is entered, loop will break out to here
print ("End try loop demo. ")
