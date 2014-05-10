# the while loop will continue until an integer is entered
while True:
    try:
        # enter a number and make sure it is an integer
        firstnumber=int(input("Enter a number: "))
# if an integer has been entered, it will break out of the while loop
        break
    # if it is not an integer, an error will be thrown
    except ValueError:
        print ("not an integer number; enter it again ")

print ("Thank you for entering the number ", firstnumber)

# the while loop will continue until an integer is entered
while True:
    try:
        # enter a number and make sure it is an integer
        secondnumber = int(input("Enter a 2nd number: "))
       # if an integer has been entered, it will break out of the while loop
        break
    # if it is not an integer, an error will be thrown
    except ValueError:
        print ("Not an integer number; enter it again.")

print ("Thank you for entering the number ", secondnumber)

product = firstnumber * secondnumber
print ("The product of the 2 numbers is: ", product)
