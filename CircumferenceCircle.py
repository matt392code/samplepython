print ("This will calculate the circumference of a circle.")
pi = 3.141592
print ("Pi is:", pi)

DiameterEntered = input("Please enter the diameter: ")

# Converting diameter to a floating number
DiameterFloat = float(DiameterEntered)

# Calculating the circumference of a circle
circumference = pi*DiameterFloat
print ("The circumference is: ", circumference)
