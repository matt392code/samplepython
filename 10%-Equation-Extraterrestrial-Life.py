# Program that will estimate the number of stars with extraterrestrial life
# within a given number of stars
# Please note that this is more of a thought experiment than it is scientifically accurate

def tenpercent(number):
    tenpercentofnumber = number * .1
    return tenpercentofnumber

def numberofstars():
    starsentered = input("Please enter the number of stars in a given region of space: ")
    stars = float(starsentered)
    return stars

# Call number of stars function
numberofstarsentered = numberofstars()
print("The number of stars entered is: ", numberofstarsentered)

# Start the 10 percent calculations

# Calculate the number of stars capable of supporting life
numberofstarscapableofsupportinglife = tenpercent(numberofstarsentered)
print("The number of stars capable of supporting life: ", numberofstarscapableofsupportinglife)

# Calculate the number of stars where life of any kind actually develops
numberofstarslifedevelops = tenpercent(numberofstarscapableofsupportinglife)
print("Number of stars where life of any kind develops ", numberofstarslifedevelops)

# Calculate the number of stars where complex life develops
numberofstarscomplexlife = tenpercent(numberofstarslifedevelops)
print("Number of stars where complex life develops ", numberofstarscomplexlife)

# Calculate the number of stars where intelligent life develops
numberstarsintelligentlife = tenpercent(numberofstarscomplexlife)
print("Number of stars where intelligent life develops: ", numberstarsintelligentlife)

# Calculate the number of stars where basic technology is developed
numberstarstechnology = tenpercent(numberstarsintelligentlife)
print("Number of stars where basic technology is developed: ", numberstarstechnology)

# Calculate the number of stars where interstellar travel technology is developed
numberstarsinterstellartravel = tenpercent(numberstarstechnology)
print("Number of stars that develop interstellar travel technology: ", numberstarsinterstellartravel)

