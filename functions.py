Picture of Python Programming - functions
#Using functions

# Basic function that prints a statement
def hello():
    print ("Hello world!")
# Call the function
hello()

print("===================")

# Function that returns a value
def whatispi():
    return 3.14159
# Call the function
print ("Pi is:", whatispi() )

print("===================")

# Function that calculates using a formula
def area(length, width):
    area = length * width
    print ("The area is:", area)
# Call the function with arguments
area(9,8)

print("===================")

# Function that calculates but provides more information
def areawithinfo(length, width):
    area = length * width
    print ("Length is:", length)
    print ("Width is:", width)
    print ("Total area is:", area)
# Call the function with arguments
areawithinfo(9,8)

print("===================")

# Function that returns a value
def areareturn(length, width):
    area = length * width
    return area
# Call a function with arguments.
# Then take the return value and place it into a variable
computerroom = areareturn (9,8)
print ("The area of the computer room is:", computerroom)

print ("================")
# Calling 2 functions

def roomarea(length, width):
    area = length*width
    return area
   
def roomvolume(area, height):
   volume = area*height
   return volume
   
area = roomarea(9,8)
finalvolume = roomvolume(area,10)
print ("The volume is: ", finalvolume)

print ("================")

# Function calling other functions
def callother(length, width):
     hello()
     whatispi()
     area(length, width)

callother (9, 10)
