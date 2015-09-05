# Released under the GPL
print ("Newton's Method.")
print ("This program will determine a square root using Newton's Method.")

numberentered = input("Enter a number: ")
# Convert the entered string into a float number
number = float(numberentered)

# Define the function that uses Newton's Method
def square_root(number):
    estimate = number/2
    # print ("The initial estimate is: ", estimate)
    # Continue the while loop until the estimate and newestimate variables are equal,
    # then break out of the loop
    while True:
            print("Calculating new estimate using Newton's Method.")
            newestimate = ((estimate+(number/estimate))/2)
            print("The current estimate is:",   estimate)
            if newestimate == estimate:
                print("Found the square!",  newestimate)
                break # break out of loop here
            print ("New estimate is:",  newestimate)
            # Assign newestimate value to estimate
            estimate = newestimate
    # End while loop
    
square_root(number)
print ("Exiting program now.")
